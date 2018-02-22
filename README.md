# ITFest-Reservation

This project was developed at the ITFest 12 hours hackathon on 11 November 2017 at 360HUB. The task was given by the Microsoft team on Azure Cloud department.
The project purpose was to facilitate the table reservations of a restaurant. We had to analyse the clients messages by parsing them 
and look for key words like the reservation hour, number of persons and if that client prefer a specific kind of food. 
Also, we had to use emotion API to analyse the emotions that the client wants to induce from his message, if he's happy, angry etc.
If the client reservation was approved, a confirmation mail had to be sent to that client. After that we made a user interface where we could see all approved reservations, sort them after day or hours and check their informations.

The backend of the app was made in python and the UI was made in ASP.NET MVC app. Both of them used azure cosmos db NoSQL database for saving the data.
My part was mainly the ASP.NET MVC part for user interface.
