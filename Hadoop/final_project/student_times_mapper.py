#!/usr/bin/python
import csv
import sys

reader = csv.reader(sys.stdin, delimiter="\t")
headers=reader.next()
for line in reader:
	print "{0}\t{1}".format(line[3],line[8])

