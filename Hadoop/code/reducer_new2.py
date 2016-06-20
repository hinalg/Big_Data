#!/usr/bin/python

import sys

hitCount = 0
wantedIP="10.99.99.186"

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisKey, count = data_mapped
    if thisKey == wantedIP:
	hitCount+=1
if hitCount == 0:
   print "??","\t","??"
else:
   print wantedIP,"\t", hitCount

