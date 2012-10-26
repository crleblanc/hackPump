#!/usr/bin/env python
#
# Stripped down version of Google example for event list, doesn't need oauth since we're 
# reading from a public calendar so isn't required.

from datetime import datetime, date, timedelta
# available from pip
import pyrfc3339
import pytz 
import httplib2
from apiclient.discovery import build

def current_calendar_events(calId, time_window=1):

    http = httplib2.Http()
    service = build(serviceName='calendar', version='v3', http=http,
                    developerKey='AIzaSyA96dI1CPIUEuzgi3-_H8dQVyM34rak5vE')

    # get a list of all events +/- the specified number of days from now
    now = datetime.utcnow().replace(tzinfo=pytz.utc)
    diffTime = timedelta(days=time_window)
    queryStart = now - diffTime
    queryEnd = now + diffTime

    dayStartString = pyrfc3339.generate(queryStart)
    dayEndString = pyrfc3339.generate(queryEnd)

    events = service.events().list(calendarId=calId, singleEvents=True, timeMin=dayStartString, timeMax=dayEndString, orderBy='updated').execute()

    eventList = []
    for event in events['items']:
        endTime = pyrfc3339.parse(event['end']['dateTime'])
        startTime = pyrfc3339.parse(event['start']['dateTime'])
        
        if now > startTime and now < endTime:
            eventList.append(event)
        
    return eventList
