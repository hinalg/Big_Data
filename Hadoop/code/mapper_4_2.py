#!/usr/bin/python

# Format of each line is:
# We want elements 2 (word) and 4 (id)
# We need to write them in word --id form

import sys
import csv
import re
body_splitter= re.compile(r'[\.,!?\:;\"\(\)\<\>\[\]#$\=\-\/\s]')
tsv_reader =csv.reader(sys.stdin, delimiter="\t")
next(tsv_reader, None) #skipping the header
for row in tsv_reader:
	id=row[0]
	body=row[4]
	words=re.split(body_splitter,body)
	for word in words:
		if word!="" and len(word)>0:
			print "{0}\t{1}".format(word,id)


