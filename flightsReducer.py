from operator import itemgetter
import sys
import json

(last_key, total) = (None, 0)
for line in sys.stdin:
   (tempKey, tempVal) = line.strip().split('\t')
   (key, val) = (tempKey, json.loads(tempVal))
   if last_key and last_key != key:
        #Means we are seeing a new key
        print '%s\t%s' %(last_key, total)
        (last_key, total) = (key, (float(val[4])))
   else:
        (last_key, total) = (key, (float(val[4])) + total)

if last_key:
    print '%s\t%s' %(last_key, total)
