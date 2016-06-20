#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys
import re


for line in sys.stdin:
   ip = ""
   data = re.compile(r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}')
   ip_match = data.match(line)
   if ip_match:
	ip=ip_match.group(0)
  	print "{0}\t{1}".format(ip,"1")

