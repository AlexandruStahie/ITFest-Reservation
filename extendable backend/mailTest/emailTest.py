import sendgrid
import os

senderEmail = "foodliciousro@outlook.com"
receiverEmail = "andadrn@gmail.com"

sg = sendgrid.SendGridAPIClient(apikey='SG.gBEE_Tk_Q26Wv5FvgmR5uw.fKukvKmuTj6TfxkQ5L_7uHY9vr2xrUvVZVrSSny5-HY')
data = {
  "personalizations": [
    {
      "to": [
        {
          "email": receiverEmail
        }
      ],
      "subject": "Reservation response"
    }
  ],
  "from": {
    "email": senderEmail
  },
  "content": [
    {
      "type": "text/plain",
      "value": "and easy to do anywhere, even with Python"
    }
  ]
}
response = sg.client.mail.send.post(request_body=data)
print(response.status_code)
print(response.body)
print(response.headers)