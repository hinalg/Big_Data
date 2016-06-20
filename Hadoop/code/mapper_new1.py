#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re


for line in sys.stdin:
   url = ""
   # first lets split by quotes
   data = line.strip().split('"') 
   if len(data)!=3: 
	#misformed log- missing url
	continue
   else:# len(data)==3:
	req=data[1].strip().split()
	if len(req)!=3:
	    continue
	url=req[1]
   print "{0}\t{1}".format(url,"1")

