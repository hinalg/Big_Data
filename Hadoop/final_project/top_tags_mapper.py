#!/usr/bin/python
import csv
import sys
reader = csv.reader(sys.stdin, delimiter="\t")
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
headers= reader.next()
tag_counter=dict()
for line in reader:
	type_of_node=line[5]
	if type_of_node.lower() == "question":
        	tags= line[2]
        	if tags and len(tags)>0:
            		indi_tag=tags.split(" ")
            		for t in indi_tag:
				if t in tag_counter:
					tag_counter[t]+=1
				else:
				        tag_counter[t]=1
top=0
for w in sorted(tag_counter,key=tag_counter.get,reverse=True):
	if top ==10:
		break                		
	print "{0}\t{1}".format(w,tag_counter[w])
	top+=1
