# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 18:49:32 2016

@author: sahebsingh
"""

states= {
    'Oregon': 'OR',
    'Florida':'FL',
    'California':'CA',
    'New York':'NY',
    'Michigan':'MI'
}
#Create basic set of states and some cities in them
cities={
     'OR': 'San Francisco',
     'MI':'Detroid',
     'FL':'Jacksonville'
}
#add some more cities
states['New Jersey']='NW'
cities['NY']='New York'
cities['OR']='Portland'

#print out some cities
print('_' *10)
print("NY state has:",cities['NY'])
print("OR state has:",cities['OR'])

#print some states

print('_' *10)
print("MIchigan's abbreviation is",states['Michigan'])
print("Florida's abbreviation is",states['Florida'])

#do it by usng states than cities dict
print('_' *10)
print("Michigan has:",cities[states['Michigan']])
print("Florida has:",cities[states['Florida']])
#print("Florida has:",cities['FL'])

#print every state abbrivation
print('_' *10)
for state,abbrev in states.items():
    print("%s state has %s abbreviation:"%(state,abbrev))

#print every city in the state
print('_' *10)
for abbrev,cities in cities.items():
    print("%s has %s cities"%(abbrev,cities))

#we can do both at the same time
#print('_' *10)
#for state,abbrev in states.items():
#    #print(type(abbrev))
#    print("%s has %s abbreviation and %s cities"%(state,abbrev,cities[abbrev]))
   
#safely get an abbreviation by the state that ight not be there
state=states.get('Texas',None)

if not state:
    print("Sorry no Texas")

#get a city with default value
city=cities.get('TX','Does ot exist')
print("The city for the state 'TX'%s"%city)
print(cities['NY'])






