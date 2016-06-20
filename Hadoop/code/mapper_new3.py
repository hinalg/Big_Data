#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re


for line in sys.stdin:
   filepath=None
   url=None
   # first lets split by quotes
   data = line.strip().split('"') 
   if len(data)==3:
	access_request=data[1].strip().split()
	url=access_request[1] 
	if url.startswith("http",0):
	   filepath_m=re.search(r'\w{4,5}:[/]{2}[a-zA-Z0-9_\-.]+(?P<fp>/.*)',url)
           if filepath_m:
		filepath=filepath_m.group('fp')
	else:
	   filepath=url
        print "{0}\t{1}".format(filepath,1)

