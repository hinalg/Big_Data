#!/usr/bin/python	

import sys

student_dict={} #per student data
oldKey= None
max_value= 0
for l in sys.stdin:
	data_mapped= l.strip().split("\t")
	if len(data_mapped) !=2:
		continue
	k,v=data_mapped
	hour=v.split(" ")[1].split(":")[0]
        if oldKey and oldKey != k:
                #print last guy's data
		for k1,v1 in student_dict.iteritems():
			if v1==max_value:
				print "{0}\t{1}".format(oldKey,k1)
		#NEW GUY
		oldKey=k
		student_dict={}
		max_value=0
	oldKey=k
	if hour in student_dict:
		student_dict[hour]+=1
	else:	
		student_dict[hour]=1
	
	if student_dict[hour]>=max_value:
		max_value= student_dict[hour]

