#!/usr/bin/python

import sys
#day:[count,total]
spending={'0':[0,0.0],'1':[0,0.0],'2':[0,0.0],'3':[0,0.0],'4':[0,0.0],'5':[0,0.0],'6':[0,0.0]}
#Monday-Sunday
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

    thisKey, thisSale = data_mapped
    if thisKey in spending:
	spending[thisKey][0]+=1
	spending[thisKey][1]+=float(thisSale)

for k,v in spending.iteritems():
    if v[0] != 0:
    	print "{0}\t{1}".format(k,v[1]/float(v[0]))
    #else:
    #	print "{0}\t{1}".format(k,0)

