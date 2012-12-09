#!/usr/bin/python
from operator import itemgetter
import sys
import json

"""
    A genric reducer that will take the incoming flight record and
    will calculate total records for a given destination
"""

(last_key, total) = (None, 0)
counter = 0
for line in sys.stdin:
   (tempKey, tempVal) = line.strip().split('\t')
   (key, val) = (tempKey, json.loads(tempVal))
   if last_key and last_key != key:
        #Means we are seeing a new key
	#We print out the last record and its total count
        print '%s\t%s' %(last_key, (total,counter))
        counter =  1
        (last_key, total) = (key, (float(val[4])))
   else:
        #We enter here for the very first time when the key is NONE
        #or when the key is not changing
        counter = counter + 1
        (last_key, total) = (key,((float(val[4])) + total))

if last_key:
    #This takes care of the last key if last key is unique
    #TODO Possible bug with the counter here
    #NOTE:The counter will always be 1 here as this was the last key which was different
    print '%s\t%s' %(last_key, (total,counter))
