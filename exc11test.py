#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ΓΙΟΥΛΙΑΝ ΠΡΟΚΟ
#Π16119
#Κάποιες φορές μπορει να καθυστερήσει λίγο έως αρκετά η αποστολή e-mail. Εάν συμβαίνει κάτι τέτοιο ξαναπροσπαθήστε να εκτελέσετε το πρόγρσμμα.
#Ειδάλως βαθμολογείστε τον κώδικα.
#Proper libraries
import urllib2
import json
import re
import requests
#e-mail by user
user_email=raw_input("insert an e-mail: ")
user_email=str(user_email)
#fetch beer
api_random_beer=urllib2.urlopen("https://api.punkapi.com/v2/beers/random")
#make it readable
api_random_beer=api_random_beer.read()
api_random_beer=json.loads(api_random_beer)
beer_id=api_random_beer[0]["id"]
beer_id=str(beer_id)
beer_name=api_random_beer[0]["name"]
beer_name=str(beer_name)
beer_description=api_random_beer[0]["description"]
beer_description=str(beer_description)
text="Your beer of the day is here.\n Made it possible by https://punkapi.com.\n Developed by Juljan Proko \n Id: "+beer_id+"\n Beer Name:"+beer_name+"\n "+ beer_description+" "
text=str(text)
def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandboxa99895715fa249d8abb3b872898c2dd7.mailgun.org/messages",
        auth=("api", "key-d971ef34fe87ea5bc26c3bd290bc4438"),
        data={"from": "<juljanproko3@gmail.com>",
              "to": "<"+user_email+">",
              "subject": "The beer of the day",
              "text":text })

send_simple_message();
print "stalthike"
