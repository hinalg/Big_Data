#!/usr/bin/python
import csv
import sys

reader = csv.reader(sys.stdin, delimiter="\t")
headers=reader.next()
for line in reader:
	if line[5].lower()=="question": 
		print "{0}\t{1}".format(line[0],line[3])
	else:#get absparent_id
		if line[7]!=None or line[7]!="":
			print "{0}\t{1}".format(line[7],line[3])
		else:
			print "{0}\t{1}".format(line[6],line[3])

