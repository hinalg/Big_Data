#!/usr/bin/python

import sys

word = "fantastically"
set_of_nodes=set()
for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong. Skip this line.
        continue
    thisKey, thisId = data_mapped
    if word == thisKey:
	set_of_nodes.add(thisId)

print "fantastically", "\t",set_of_nodes 

