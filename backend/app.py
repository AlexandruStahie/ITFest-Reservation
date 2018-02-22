import datetime
from cmath import sqrt
from collections import defaultdict

from azure.storage.queue import QueueService
from emotion import *
from no_people import *
from name_parser import *
from food_parser import *
from email_sender_cl import *

login_info = {
    'account': {
        'name': 'itfest2017',
        'key': '1bS7zBgC2yeK2ipb+XUanT6ZDL/QCdVdwBluoCn8ao4WI+F3g6UGZoDhy0hXTWjSksPCbXXFhSXSbSuZMQrkYA=='
    },
    'queue': 'codelicious',
    'functions-middle': 'https://reservation-codelicious.azurewebsites.net/api/reservation-middle'
}

queue_service = QueueService(account_name=login_info['account']['name'], account_key=login_info['account']['key'])


already_res = defaultdict(int)


def can_res(date, no_people):
    hdate = date.split(':')[0]

    old_no_people = already_res[hdate]
    if old_no_people + no_people <= 80:
        already_res[hdate] += no_people
        return True
    else:
        return False


while True:
    def get_raw_messages():
        messages = queue_service.get_messages(login_info['queue'])
        messages_reformat = []

        for message in messages:
            message_r = json.loads(message.content)
            message_r['id'] = message.id
            #message_r['date'] = datetime.datetime.strptime(message_r['date'], "%Y-%m-%d %H:%M")
            message_r['insertion_time'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
            message_r['expiration_time '] = message.expiration_time.strftime("%Y-%m-%d %H:%M")
            message_r['no_people'] = get_no_people(message_r['message'])
            message_r['name'] = get_name(message_r['message'])
            message_r['emotion'] = get_emotion(message_r['message'])
            message_r['prefferences'] = get_prefferences(message_r['message'])

            if can_res(message_r['date'], int(message_r['no_people'])):
                messages_reformat.append(message_r)
                send_mail(message_r['email'], message_r['name'], message_r['emotion'], True)
            else:
                send_mail(message_r['email'], message_r['name'], message_r['emotion'], False)

            queue_service.delete_message(login_info['queue'], message.id, message.pop_receipt)

        return messages_reformat


    for message in get_raw_messages():
        print(message)
        #r = requests.post(login_info['functions-middle'], data=message)
        r = requests.get(login_info['functions-middle'], params=message)
