from azure.storage.queue import QueueService
import json

login_info = {
    'account': {
        'name': 'itfest2017',
        'key': '1bS7zBgC2yeK2ipb+XUanT6ZDL/QCdVdwBluoCn8ao4WI+F3g6UGZoDhy0hXTWjSksPCbXXFhSXSbSuZMQrkYA=='
    },
    'queue': 'codelicious'
}

queue_service = QueueService(account_name=login_info['account']['name'], account_key=login_info['account']['key'])

messages = [
    {
        "date": "2017-07-20 12:30",
        "email": "andadrn@gmail.com",
        "message": "fu, i'm Mihai Despotovici, give me a table for 7. I love your restaurant"
    },
    {
        "date": "2017-07-20 12:30",
        "email": "andadrn@gmail.com",
        "message": "i John am I want a table of 400 at 8. I do not like you"
    },
    {
        "date": "2017-07-20 12:45",
        "email": "andadrn@gmail.com",
        "message": "I want a table of 4. I was not happy about your services."
    },
    {
        "date": "2017-07-20 12:46",
        "email": "andadrn@gmail.com",
        "message": "We are Anda and Mihai and we want a table of 400 at 8. We will want some pork pie and calamari when i come, please"
    },
    {
        "date": "2017-07-20 09:30",
        "email": "andadrn@gmail.com",
        "message": "We are Anda and Mihai and we want a table of 4 at 8. We will want some pork pie and calamari when i come, please"
    },
    {
        "date": "2017-07-20 09:00",
        "email": "andadrn@gmail.com",
        "message": "I want a table of 8. I want to eat calamari"
    },
]

for message in messages:
    queue_service.put_message(login_info['queue'], json.dumps(message))