#!/usr/bin/python
import sys
import Queue
count=0
oldKey=None
pq=Queue.PriorityQueue(maxsize=10)
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
	continue
    thisKey,val=data_mapped
    if oldKey and oldKey!= thisKey:
        #print old guy's stuff
        if not pq.full():
		pq.put((count,oldKey))
        else:
	        lowest=pq.get()	
	       	if count>lowest[0]:
			#Put in this entry
			pq.put((count,oldKey))
		else:#Put the popped entry back
			pq.put((lowest[0],lowest[1]))
	#reinitialize for the new guy
	count=0 
    oldKey=thisKey
    count+=int(val)
if oldKey:
   if not pq.full():
   	pq.put((count,oldKey))
   else:
        lowest=pq.get()         
        if count>lowest[0]:
                        #Put in this entry
                        pq.put((count,oldKey))
        else:#Put the popped entry back
                        pq.put((lowest[0],lowest[1]))

while not pq.empty():
	x=pq.get()
	print "{0}\t{1}".format(x[1],x[0])
