#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ΓΙΟΥΛΙΑΝ ΠΡΟΚΟ
#Π16119
#Proper libraries
import urllib2
import json
import re


user_request_currency_to=[]
user_request_currency_from=raw_input('Insert your currency to be converted: ')
user_request_currency_from=user_request_currency_from.upper()
user_request_currency_number=raw_input('How many currencies you want to get result? ')
user_request_currency_number=int(user_request_currency_number)
for i in range(0,user_request_currency_number):
    user_request_currency_to_insert=raw_input('Insert your currency to be converted: ')
    user_request_currency_to_insert=user_request_currency_to_insert.upper()
    user_request_currency_to.append(user_request_currency_to_insert)

user_request_date=raw_input('Insert date/timezone Athens/in form (year-month-day): ')
url_epoch_converter="http://www.convert-unix-time.com/api?date="+user_request_date+"&timezone=athens"
#fetch date converter data
api_epoch_converter=urllib2.urlopen(url_epoch_converter)
#make it readable
api_epoch_converter=api_epoch_converter.read()
#make it dict
api_epoch_converter=json.loads(api_epoch_converter)
timestamp=api_epoch_converter['timestamp']
timestamp=str(timestamp)
prices=[]
#for coins in range(0,user_request_currency_number):
for i in range(0,user_request_currency_number):
    url_currency="https://min-api.cryptocompare.com/data/pricehistorical?fsym="+user_request_currency_from+"&tsyms="+user_request_currency_to[i]+"&ts="+timestamp
    #fetch coin data
    api_coin_data=urllib2.urlopen(url_currency)
    api_coin_data=api_coin_data.read()
    api_coin_data=json.loads(api_coin_data)
    timi=api_coin_data[user_request_currency_from][user_request_currency_to[i]]
    prices.append(timi)

#bubble short
for i in range(0,user_request_currency_number-1):
    for j in xrange(user_request_currency_number-1,i,-1):
        if (prices[j] < prices[j-1]):
            temp1=prices[j]
            prices[j]=prices[j-1]
            prices[j-1]=temp1
            temp2=user_request_currency_to[j]
            user_request_currency_to[j]=user_request_currency_to[j-1]
            user_request_currency_to[j-1]=temp2

print "Results:"
print "Date: "+user_request_date
print "From: "+user_request_currency_from
for i in range(0,user_request_currency_number):
    prices[i]=str(prices[i])
    print "To "+user_request_currency_to[i]+" is "+prices[i]
