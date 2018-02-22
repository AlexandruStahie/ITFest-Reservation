using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using Newtonsoft.Json;

namespace ITFest.Models
{
    public class Reservation
    {

        [JsonProperty(PropertyName = "id")]
        public string Id { get; set; }

        [JsonProperty(PropertyName = "date")]
        public DateTime? Date { get; set; }

        [JsonProperty(PropertyName = "email")]
        public string Email { get; set; }

        [JsonProperty(PropertyName = "message")]
        public string Message { get; set; }

        [JsonProperty(PropertyName = "name")]
        public string Owner { get; set; }

        [JsonProperty(PropertyName = "no_people")]
        public int? NrOfPersons { get; set; }

        public bool? Status { get; set; }

        [JsonProperty(PropertyName = "insertion_time")]
        public DateTime? StartReservationDate { get; set; }
        [JsonProperty(PropertyName = "expiration_time")]
        public DateTime? EndReservationDate { get; set; }

        [JsonProperty(PropertyName = "prefferences")]
        public string Prefferences { get; set; }

        [JsonProperty(PropertyName = "emotion")]
        public string Emotion { get; set; }


        public int? NrOfFreeSpaces { get; set; }
        public int TableNumber { get; set; }
        public string TableLink { get; set; }

        public string StartToString { get; set; }
        public string EndToString { get; set; }

    }
}

