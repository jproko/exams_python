#!/usr/bin/env python
# -*- coding: utf-8 -*-
#ΓΙΟΥΛΙΑΝ ΠΡΟΚΟ
#Π16119
#Κάποιες φορές μπορει να βγάλει error γιατι το structure μερικων API'S fetch είναι ελαφρώς διαφορετικά απο το βασικό(Θεωρητικά τρέχει) 
#Proper libraries
import urllib2
import json
import re

#create dictionary of results of our desire
dict_results={}
print 'Beer Data Base is being loaded. Please have patience while dreaming your favourite beer...'
#Λογώ του ότι δεν σε αφήνει να κανεις fetch ολες τις μπύρες, κάνω fetch μονο 50 για την εκτελεση του προγραμματος
for i in range(0,25):
    if (i==5):
        print "25%"
    elif(i==10):
        print "50%"
    elif (i==15):
        print "75%"
    #fetch data
    api_search=urllib2.urlopen('https://api.brewerydb.com/v2/beer/random?key=f491f953ea5b5aaae0656001936028c0&format=json')
    #make it readable
    api_search=api_search.read()
    api_search.encode('ascii', 'ignore')
    #initialize variables in case of (false) in if structures bellow
    api_search_data='No data Found.'
    api_search_data_name='No Name Found.'
    api_search_data_abv='No abv Found.'
    api_search_data_isOrganic_res='We could no find if this beer is Organic or not.'
    api_search_data_style='No style Found'
    api_search_data_style_ibu_ave='No IBU Found.'
    api_search_data_style_name='No style name found.'
    api_search_data_style_fg_ave='No FG Found.'
    api_search_data_style_srm_ave_color='No Beer Color Found.'
    api_search_data_style_description='No Description Found.'
    #check one dictionart at a time if (what we want) exist
    if ('data' in api_search):
        api_search_data=json.loads(api_search)['data']
        if('name' in api_search_data):
            api_search_data_name=json.loads(api_search)['data']['name']
        if('abv' in api_search_data):
            api_search_data_abv=json.loads(api_search)['data']['abv']
            api_search_data_abv= 'The alchochol by volume (abv) is '+api_search_data_abv+'% .'
        if('isOrganic' in api_search_data):
            api_search_data_isOrganic=json.loads(api_search)['data']['isOrganic']
            if('Y' in api_search_data_isOrganic):
                api_search_data_isOrganic_res= 'Your beer is organic.'
            else:
                api_search_data_isOrganic_res= 'Your beer is not-organic.'
        if('style' in api_search_data):
            api_search_data_style=json.loads(api_search)['data']['style']
            if ('name' in api_search_data_style):
                api_search_data_style_name=json.loads(api_search)['data']['style']['name']
                api_search_data_style_name='This beer belongs to '+api_search_data_style_name+'style family.'
            if ('description' in api_search_data_style):
                api_search_data_style_description=json.loads(api_search)['data']['style']['description']
            if (('ibuMin' and 'ibuMax') in api_search_data_style):
                api_search_data_style_ibu_min=json.loads(api_search)['data']['style']['ibuMin']
                api_search_data_style_ibu_max=json.loads(api_search)['data']['style']['ibuMax']
                api_search_data_style_ibu_min=int(api_search_data_style_ibu_min)
                api_search_data_style_ibu_max=int(api_search_data_style_ibu_max)
                api_search_data_style_ibu_ave=(api_search_data_style_ibu_min+api_search_data_style_ibu_max)/2
                api_search_data_style_ibu_ave=str(api_search_data_style_ibu_ave)
                api_search_data_style_ibu_ave='The international bitterness units (ibu) of the Beer is '+api_search_data_style_ibu_ave+'.'
            if (('fgMin' and 'fgMax') in api_search_data_style):
                api_search_data_style_fg_min=json.loads(api_search)['data']['style']['fgMin']
                api_search_data_style_fg_max=json.loads(api_search)['data']['style']['fgMax']
                api_search_data_style_fg_min=float(api_search_data_style_fg_min)
                api_search_data_style_fg_max=float(api_search_data_style_fg_max)
                api_search_data_style_fg_ave=(api_search_data_style_fg_min+api_search_data_style_fg_max)/2
                api_search_data_style_fg_ave=str(api_search_data_style_fg_ave)
                api_search_data_style_fg_ave='The final gravity (fg) of the Beer is '+api_search_data_style_fg_ave+'.'
            if (('srmMin' and 'srmMax') in api_search_data_style):
                api_search_data_style_srm_min=json.loads(api_search)['data']['style']['srmMin']
                api_search_data_style_srm_max=json.loads(api_search)['data']['style']['srmMax']
                api_search_data_style_srm_min=int(api_search_data_style_srm_min)
                api_search_data_style_srm_max=int(api_search_data_style_srm_max)
                api_search_data_style_srm_ave=(api_search_data_style_srm_min+api_search_data_style_srm_max)/2
                if(api_search_data_style_srm_ave<3):
                    color='pale straw'
                elif(api_search_data_style_srm_ave<4):
                    color='straw'
                elif(api_search_data_style_srm_ave<6):
                    color='pale gold'
                elif(api_search_data_style_srm_ave<9):
                    color='deep gold'
                elif(api_search_data_style_srm_ave<12):
                    color='pale amber'
                elif(api_search_data_style_srm_ave<15):
                    color='medium amber'
                elif(api_search_data_style_srm_ave<18):
                    color='deep amber'
                elif(api_search_data_style_srm_ave<20):
                    color='amber brown'
                elif(api_search_data_style_srm_ave<24):
                    color='brown'
                elif(api_search_data_style_srm_ave<30):
                    color='ruby brown'
                elif(api_search_data_style_srm_ave<40):
                    color='ruby brown'
                else:
                    color='black'
                    api_search_data_style_srm_ave_color= 'The color of the Beer is '+color+'.'

    #converting json to text before inserting in our dictionary
    api_search_data_style_description=api_search_data_abv+api_search_data_isOrganic_res+api_search_data_style_name+api_search_data_style_ibu_ave+api_search_data_style_fg_ave+api_search_data_style_srm_ave_color+api_search_data_style_description
    dict_results.update({api_search_data_name:[api_search_data_style_description]})
user_request=raw_input('Insert your request key words seperated by comma(i.e. American,organic,brown) max=8: ')
user_request_list=re.split(',',user_request)
i=7
while True:
    try:
        akiri_metavliti=user_request_list[i]
        arithmos_leksewn=i+1
        break
    except IndexError:
        i=i-1
arithmos_leksewn=int(arithmos_leksewn)
vrethike=False
for k in dict_results:
    for v in dict_results[k]:
        if(arithmos_leksewn==1):
            if (user_request_list[0] in v):
                print k
                vrethike=True
        elif(arithmos_leksewn==2):
            if ((user_request_list[0] and user_request_list[1]) in v):
                print k
                vrethike=True
        elif(arithmos_leksewn==3):
            if ((user_request_list[0] and user_request_list[1] and user_request_list[2]) in v):
                print k
                vrethike=True
        elif(arithmos_leksewn==4):
            if ((user_request_list[0] and user_request_list[1] and user_request_list[2] and user_request_list[3]) in v):
                print k
                vrethike=True
        elif(arithmos_leksewn==5):
            if ((user_request_list[0] and user_request_list[1] and user_request_list[2] and user_request_list[3] and user_request_list[4]) in v):
                print k
                vrethike=True
        elif(arithmos_leksewn==6):
            if ((user_request_list[0] and user_request_list[1] and user_request_list[2] and user_request_list[3] and user_request_list[4] and user_request_list[5]) in v):
                print k
                vrethike=True
        elif(arithmos_leksewn==7):
            if ((user_request_list[0] and user_request_list[1] and user_request_list[2] and user_request_list[3] and user_request_list[4] and user_request_list[5] and user_request_list[6]) in v):
                print k
                vrethike=True
        elif(arithmos_leksewn==8):
            if ((user_request_list[0] and user_request_list[1] and user_request_list[2] and user_request_list[3] and user_request_list[4] and user_request_list[5] and user_request_list[6] and user_request_list[7]) in v):
                print k
                vrethike=True
if(vrethike==False):
    print 'No request Found'
