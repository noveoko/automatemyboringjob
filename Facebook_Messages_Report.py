import json
from datetime import datetime, timezone
import glob
from pathlib import Path
import os


times = []

files = glob.glob("**/*.json")

print(files)

import datetime,pytz

def getTime(milliseconds, timezone="US/Central"):
    dtobj2 = datetime.datetime.fromtimestamp(milliseconds/1000.0)


    mytimezone=pytz.timezone("Europe/Warsaw") #my current timezone
    dtobj4=mytimezone.localize(dtobj2)        #localize function

    new_timezone=dtobj4.astimezone(pytz.timezone(timezone)) #astimezone method
    return [timezone, new_timezone.date(), new_timezone.time()]


def participants(list_of_people):
    if len(list_of_people) > 4:
        return f"{list_of_people[0:4]}_..."
    else:
        return list_of_people

for file in files:
    with open(file,'r',encoding='utf-8') as outfile:
        j = json.load(outfile)
        for message in j["messages"]:
            ms = int(message["timestamp_ms"])
            date = datetime.datetime.fromtimestamp(ms/1000.0)
            sender = message["sender_name"]
            others = list(set([a["name"] for a in j["participants"]]))
            timeZone = getTime(ms)
            times.append([ms, sender, timeZone[1], timeZone[2], participants(others)])

with open('message_events.txt','w',encoding='utf-8') as outPut:
    for i in sorted(times,key=lambda x: int(x[0])):
        outPut.write(f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\n")
