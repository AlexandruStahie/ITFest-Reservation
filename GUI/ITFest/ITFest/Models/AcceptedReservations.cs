using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Web;

namespace ITFest.Models
{
    public class AcceptedReservations
    {

        [Display(Name = "Start Date Filter")]
        [DisplayFormat(DataFormatString = "{0:dd-MMM-yyyy hh:mm tt}", ApplyFormatInEditMode = true)]
        public DateTime StartDateFilter { get; set; }

        [Display(Name = "End Date Filter")]
        [DisplayFormat(DataFormatString = "{0:dd-MMM-yyyy hh:mm tt}", ApplyFormatInEditMode = true)]
        public DateTime EndDateFilter { get; set; }

        public List<Reservation> MyReservations { get; set; }
    }
}