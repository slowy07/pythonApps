import os
from firebase_admin import credentials, firestore, initialize_app
from datetime import datetime, timedelta
import time
from time import gmtime, strftime
import twilio
from twilio.rest import Client

accSid = ""
authToken = ""
client = Client(accSid, authToken)

cred = credentials.Certificate('key.json')
defaultApp = initialize_app(cred)
db = firestore.client()
databaseReference = db.collection('on_call')


def search():
    callingTime = datetime.now()
    oneHoursFromNow = (callingTime + timedelta(hours = 1)).strftime('%H:%M:%S')
    currentDate = str(strftime("%d-%m%Y", gmtime()))
    docs = db.collection(u'on_call').where(u'date',u'==', currentDate).stream()
    listOfDocs = []
    for doc in docs:
        c = doc.to_dict()
        if (callingTime).strftime('%H:%M:%S') <= c['from'] <= oneHoursFromNow:
            listOfDocs.append(c)
    print(listOfDocs)

    while listOfDocs:
        timestamp = datetime.now().strftime('%H:%M:%S')
        fiveMinutesPrior = (timestamp + timedelta(minutes = 5)).strftime('%H:%M:%S')
        for doc in listOfDocs:
            if doc['from'][0:5] == fiveMinutesPrior:
                phoneNumber = doc['phone']
                call = client.calls.create(
                to = phoneNumber,
                from = "add your twilio number",
                url = "http://demo.twilio.com/docs/voice.xml"
                )
                listOfDocs.remove(doc)
