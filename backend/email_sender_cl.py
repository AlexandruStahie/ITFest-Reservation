import sendgrid
import os


def send_mail(clientEmail, clientName, review, reservationStatus):
    senderEmail = "foodliciousro@outlook.com"
    receiverEmail = clientEmail
    sg = sendgrid.SendGridAPIClient(apikey='SG.gBEE_Tk_Q26Wv5FvgmR5uw.fKukvKmuTj6TfxkQ5L_7uHY9vr2xrUvVZVrSSny5-HY')

    txtMsg1 = "We are sorry for your unhappy experience! We would like to offer you a 10% discount!"
    txtMsg2 = "We are glad that you liked our restaurant! We would like to welcome you again!"

    if clientName == None:
        clientName = clientEmail
    else:
        txtMsg3 = "Your reservation is confirmed! The name on the reservation: " + str(clientName)
    txtMsg4 = "Unfortunately we do not have free tables right now! We are waiting for you to come back."

    if review == "neutral" and reservationStatus == True:
        txtMsg = txtMsg3

    if review == "neutral" and reservationStatus == False:
        txtMsg = txtMsg4

    if review == "pleased" and reservationStatus == True:
        txtMsg = txtMsg3 + " " + txtMsg2

    if review == "unpleased" and reservationStatus == False:
        txtMsg = txtMsg4 + " " + txtMsg1

    if review == "pleased" and reservationStatus == False:
        txtMsg = txtMsg4 + " " + txtMsg2

    if review == "unpleased" and reservationStatus == True:
        txtMsg = txtMsg3 + txtMsg1

    if review == "pleased":
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
                    "value": txtMsg
                }
            ]
        }
        response = sg.client.mail.send.post(request_body=data)
