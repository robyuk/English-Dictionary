#! /usr/bin/env python3
"""
Python script to ask for a word or phrase, lookup the definition in the data.json file, and print out the definition(s)

data.json is a JSON file containing keys and values, where the values are the english definitions of the keys
"""

import json

file=open('data.json')
data=json.load(file)
#print(type(data))

def define(word):
  word=word.lower()
  if word in data:
    return data[word]

word = input('Enter a word: ')
definition=define(word)
i=0
if definition:
  
  for item in definition:
    i=i+1
    print(i,item)

else:
  print('Word was not found!')