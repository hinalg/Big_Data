#!/usr/bin/python	

import sys

student_list=[] #per node student list
oldKey= None
for l in sys.stdin:
	data_mapped= l.strip().split("\t")
	if len(data_mapped) !=2:
		continue
	k,v=data_mapped
        if oldKey and oldKey != k:
                #print last guy's data
		print "{0}\t{1}".format(oldKey,student_list)
		#NEW GUY
		oldKey=k
		student_list=[]
	oldKey=k
	student_list.append(v)
if oldKey:
	print "{0}\t{1}".format(oldKey,student_list)
