#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re


for line in sys.stdin:
   ip,uid,user,access_time,url,return_code,byte_size=(None,None,None,None,None,None,None)
   # first lets split by quotes
   data = line.strip().split('"') 
   if len(data)!=3 or len(data)!=1:
	#misformed log
	continue
   elif len(data)==3:
	url=data[1]
	last_two=data[2].strip().split()
	if len(last_two)!=2:
	   # Misformed log.. 
	   continue
	return_code = last_two[0]
	byte_size = last_two[1]
   else: #len(data)==1 #missing url alltogether
        last_two=data[0].strip().split()
	if len(last_two)< 2:
	  # Misformed log continue
        else:
	    return_code=last_two[0]
	    byte_size = last_two[1]
   # common code to find the first 4  params
   date_time = re.compile(r'[\[\d{2}\/[a-zA-Z]{3}\/\d{4}:\d{2}:\d{2}:\d{2}\s-\d{4}\]')
   access_time = date_time.search(data[0])

   if access_time:
	access_time= access_time.group(0)
   else:
      # no access time continue search for ip, uid, user
      first_3 = data[0].strip().split()
      if len(first_3)< 3:
	#Misformed log
	continue
      else:
	ip=data[0]
	uid=data[1]
	user=data[2]


   print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}".format(ip,uid,user,access_time,url,retuen_code,byte_size)

