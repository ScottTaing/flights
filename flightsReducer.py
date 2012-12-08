#!/usr/bin/python
from operator import itemgetter
import sys
import json

(last_key, total) = (None, 0)
counter = 1
for line in sys.stdin:
   (tempKey, tempVal) = line.strip().split('\t')
   (key, val) = (tempKey, json.loads(tempVal))
   if last_key and last_key != key:
        #Means we are seeing a new key
        print '%s\t%s' %(last_key, (total,counter))
        (last_key, total) = (key, (float(val[4])))
        counter = counter + 1
   else:
        #We enter here for the very first time when the key is NONE
        #or when the key is not changing
        (last_key, total) = (key,((float(val[4])) + total))
        counter = counter + 1

if last_key:
    #This takes care of the last key if last key is unique
    #TODO Possible bug with the counter here
    print '%s\t%s' %(last_key, (total,counter))
