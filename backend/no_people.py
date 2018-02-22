import re

def getWords(text):
    return re.compile('\w+').findall(text)

numbers = dict([("one",1), ("two",2), ("three",3), ("four",4), ("five",5,),
                ("six",6), ("seven",7), ("eight",8), ("nine",9), ("ten",10),
                ("eleven",11), ("twelve",12), ( "thirteen",13), ("fourteen",14), ("fifteen",15),
                ("sixteen",16), ("seventeen",17), ("eighteen",18), ("nineteen",19), ("twenty",20),
                ("thirty",30), ("fourty",40), ("fifty",50)])

def get_no_people(msg):
    words = getWords(msg)

    try:
        peopleIndex = words.index("people")
    except:
        peopleIndex = None

    try:
        tableIndex = words.index("table")
    except:
        tableIndex = None

    try:
        reservationIndex = words.index("reservation")
    except:
        reservationIndex = None

    answer = None

    if (peopleIndex != None):
        for i in range(peopleIndex-1,0,-1):
            if words[i].isdigit():
                answer = words[i]
                break
            if words[i] in numbers:
                answer = numbers[words[i]]
                break

    if (tableIndex != None):
        for i in range(tableIndex+1,len(words)):
            if words[i].isdigit():
                answer = words[i]
                break
            if words[i] in numbers:
                answer = numbers[words[i]]
                break

    if (reservationIndex != None):
        for i in range(reservationIndex+1,len(words)):
            if words[i].isdigit():
                answer = words[i]
                break
            if words[i] in numbers:
                answer = numbers[words[i]]
                break

    if answer:
        return answer
    else:
        return 0