#!/usr/bin/python

import sys

d={}
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
    if thisKey in d:
	d[thisKey]+=1
    else:
	d[thisKey]=1
max_count=0
max_fp=None
#s_d=sorted(d.items(),key=d.get)
for k,v in d.iteritems():
	if v > max_count:
	   max_fp=k
	   max_count=v
print max_fp,"\t",max_count

