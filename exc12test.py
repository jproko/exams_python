#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ΓΙΟΥΛΙΑΝ ΠΡΟΚΟ
#Π16119
#Proper libraries
import urllib2
import json
import webbrowser
user_input=raw_input("What do you prefer to eat? ")
user_input=user_input.replace(" ","%20")
user_input=str(user_input)
print user_input
#fetch recipe
api_recipe=urllib2.urlopen("http://food2fork.com/api/search?key=43dc7b35c3646c78f72388182e130623&q="+user_input+"%20&page=1&sort=r")
#make it readable
api_recipe=api_recipe.read()
#make it dict
api_recipe=json.loads(api_recipe)
flag=api_recipe["count"]
if(flag!=0):
    publisher=api_recipe["recipes"][0]["publisher"]
    title=api_recipe["recipes"][0]["title"]
    source_url=api_recipe["recipes"][0]["source_url"]
    print "Published by "+publisher
    print "Title "+title
    print "Opening..."+source_url
    webbrowser.open(source_url)
    print "And the beer of the day is..."
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
    print beer_name
    print beer_description
    print "Thanks for choosing our programm for today's lunch. Good appetite and God bless you!"

else:
    print "No results found...Please check your spelling and try again."
