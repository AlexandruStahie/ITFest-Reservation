using ITFest.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using System.Net;
using System.Threading.Tasks;
using ITFest.Models;
namespace ITFest.Controllers
{
    public class ReservationController : Controller
    {
        [ActionName("Index")]
        public async Task<ActionResult> IndexAsync()
        {     
            var reservations = await DocumentDBRepository<Reservation>.GetItemsAsync();

            var resList = CalculateEndTime(reservations);

            return View(reservations);
        }

        [ActionName("AcceptedReservations")]
        public async Task<ActionResult> AcceptedReservationsAsync()
        {
            var myRes = await DocumentDBRepository<Reservation>.GetItemsAsync();

            var myResList = myRes.ToList();

            if (myResList.Count > 0 && myResList != null)
            {
                myResList.Where(x => x.Status == true);
            }

            AcceptedReservations myAcceptedReservations = new AcceptedReservations();

            myAcceptedReservations.MyReservations = myResList.ToList();
            myAcceptedReservations.StartDateFilter = DateTime.Now;
            myAcceptedReservations.EndDateFilter = DateTime.Now;

            return View(myAcceptedReservations);
        }

        [HttpPost]
        public async Task<ActionResult> FilterReservations(DateTime StartDateTime, DateTime EndDateTime)
        {
            var myRes = await DocumentDBRepository<Reservation>.GetItemsAsync();

            var myResList = CalculateEndTime(myRes);

            List<Reservation> mySecondList = new List<Reservation>();

            foreach (var x in myResList)
            {
                x.StartToString = x.Date.ToString();
                x.EndToString = x.EndReservationDate.ToString();

                bool hasEarlyStartDat = false;
                bool hasLaterEndDate = false;


                if (x.Date.HasValue)
                {
                    var Date = Convert.ToDateTime(x.Date);
                    if(DateTime.Compare(Date, StartDateTime) >= 0)
                    {
                        hasEarlyStartDat = true;
                    }
                }

                if (x.EndReservationDate.HasValue)
                {
                    var EndReservationDate = Convert.ToDateTime(x.EndReservationDate);
                    if (DateTime.Compare(EndReservationDate, EndDateTime) < 0)
                    {
                        hasLaterEndDate = true;
                    }
                }

                if (hasEarlyStartDat == true && hasLaterEndDate == true)
                {
                    mySecondList.Add(x);
                }
            }


            return Json(mySecondList);
        }

        [ActionName("GetDetails")]
        public async Task<ActionResult> GetDetails(string id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }

            Reservation item = await DocumentDBRepository<Reservation>.GetItemAsync(id);
            if (item == null)
            {
                return HttpNotFound();
            }

            if (item.EndReservationDate.HasValue == false)
            {
                double clientStayingTime = Math.Sqrt(Convert.ToInt64(item.NrOfPersons));
                clientStayingTime = Convert.ToInt32(clientStayingTime);

                var hours = Convert.ToInt32(clientStayingTime);


                if (hours + item.Date.Value.Hour > 24)
                {
                    item.EndReservationDate = new DateTime(item.Date.Value.Year,
                        item.Date.Value.Month,
                        item.Date.Value.Day,
                        Math.Abs(24 - hours),
                        item.Date.Value.Minute,
                        item.Date.Value.Second);
                    item.EndReservationDate.Value.AddDays(1);
                }
                else if (hours + item.Date.Value.Hour < 24)
                {
                    item.EndReservationDate = new DateTime(item.Date.Value.Year,
                        item.Date.Value.Month,
                        item.Date.Value.Day,
                        item.Date.Value.Hour + hours,
                        item.Date.Value.Minute,
                        item.Date.Value.Second);
                }
                else if (hours + item.Date.Value.Hour == 24)
                {
                    item.EndReservationDate = new DateTime(item.Date.Value.Year,
                     item.Date.Value.Month,
                     item.Date.Value.Day,
                     0,
                     item.Date.Value.Minute,
                     item.Date.Value.Second);
                    item.EndReservationDate.Value.AddDays(1);
                }
            }

            return View(item);
        }

        public List<Reservation> CalculateEndTime(IEnumerable<Reservation> reservations)
        {
            foreach (var res in reservations)
            {
                if (res.EndReservationDate.HasValue == false)
                {
                    double clientStayingTime = Math.Sqrt(Convert.ToInt64(res.NrOfPersons));
                    clientStayingTime = Convert.ToInt32(clientStayingTime);

                    var hours = Convert.ToInt32(clientStayingTime);


                    if (hours + res.Date.Value.Hour > 24)
                    {
                        res.EndReservationDate = new DateTime(res.Date.Value.Year,
                            res.Date.Value.Month,
                            res.Date.Value.Day,
                            Math.Abs(24 - hours),
                            res.Date.Value.Minute,
                            res.Date.Value.Second);
                        res.EndReservationDate.Value.AddDays(1);
                    }
                    else if (hours + res.Date.Value.Hour < 24)
                    {
                        res.EndReservationDate = new DateTime(res.Date.Value.Year,
                            res.Date.Value.Month,
                            res.Date.Value.Day,
                            res.Date.Value.Hour + hours,
                            res.Date.Value.Minute,
                            res.Date.Value.Second);
                    }
                    else if(hours + res.Date.Value.Hour == 24)
                    {
                        res.EndReservationDate = new DateTime(res.Date.Value.Year,
                         res.Date.Value.Month,
                         res.Date.Value.Day,
                         0,
                         res.Date.Value.Minute,
                         res.Date.Value.Second);
                         res.EndReservationDate.Value.AddDays(1);
                    }
                }
            }
            return reservations.ToList();
        }


        //[HttpPost]
        //[ActionName("Edit")]
        //[ValidateAntiForgeryToken]
        //public async Task<ActionResult> EditAsync()
        //{
        //    //iau toate inregistrarile
        //    var myRes = await DocumentDBRepository<Reservation>.GetItemsAsync();

        //    //numarul total de 
        //    int TotalNumberOfFreeSpaces = 80;

        //    var myResList = myRes.ToList();
        //    myResList.OrderBy(x => x.Date);
        //    List<Reservation> myNewResList = new List<Reservation>();

        //    foreach (var x in myResList)
        //    {
        //        bool isOK = true;

        //        foreach (var y in myNewResList)
        //        {
        //            if (DateTime.Compare())
        //        }
        //    }

        //    //pt fiecare inregistrare
        //    foreach (var res in myRes)
        //    {
        //        if (res.EndReservationDate.HasValue == false)
        //        {
        //            double clientStayingTime = Math.Sqrt(Convert.ToInt64(res.NrOfPersons));
        //            clientStayingTime = Convert.ToInt32(clientStayingTime);

        //            var hours = Convert.ToInt32(clientStayingTime / 60);
        //            var minutes = Convert.ToInt32(clientStayingTime - hours * 60);
        //            if (res.Status == null)
        //            {
        //                res.EndReservationDate = new DateTime(res.Date.Value.Year, res.Date.Value.Month, res.Date.Value.Day, res.Date.Value.Day, res.Date.Value.Hour + hours, res.Date.Value.Minute + minutes);
        //                if (TotalNumberOfFreeSpaces >= res.NrOfPersons)
        //                {
        //                    //1 = acceptata
        //                    res.Status = 1;
        //                    TotalNumberOfFreeSpaces -= Convert.ToInt32(res.NrOfPersons);
        //                }
        //                else if (TotalNumberOfFreeSpaces < res.NrOfPersons)
        //                {
        //                    //2 = refuzata
        //                    res.Status = 2;
        //                }
        //            }
        //            //timpul de expirare a rezervarii e > data si timpul curent
        //            else if (res.Status == 1 && DateTime.Compare(Convert.ToDateTime(res.EndReservationDate), DateTime.Now) <= 0)
        //            {
        //                //a trecut timpul rezervarii, posibil ca oamenii sa fi fost sau nu la masa
        //                res.Status = 3;
        //                TotalNumberOfFreeSpaces += Convert.ToInt32(res.NrOfPersons);
        //            }
        //        }



        //        ///

        //        //foreach (var res in myResList)
        //        //{
        //        //    if()
        //        //    await DocumentDBRepository<Reservation>.UpdateItemAsync(item.Id, item);

        //        //}


        //        return RedirectToAction("Index");

        //    }

        }
    }