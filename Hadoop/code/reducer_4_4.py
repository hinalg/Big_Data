#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys

def reducer():
    oldKey=None
    usr_record=[None for i in xrange(0,4)]
    node_records=[]
    for line in sys.stdin:
      line=line.replace('"','')
      #print "line-->"+line
      fields=line.split("\t")
      thisKey=fields[0]
      #print "fields is --->"+str(fields)
      if oldKey and  thisKey != oldKey:
         #getting the first record for this key --dump record for previous key
         for record in node_records:
           print "{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}".format(record[0],record[1],record[2],oldKey,record[3],record[4],record[5],record[6],record[7],usr_record[0],usr_record[1],usr_record[2],usr_record[3])
         #reset the record
         usr_record=[None for i in xrange(0,4)]
         node_records=[]
      
      oldKey= fields[0]
      if fields[1]=="A":
         usr_record[:]=fields[2:]
         #print "user record--->"+str(usr_record)
      else:
         #print "adding node record-->"+str(fields[2:10])
         node_records.append(fields[2:10])

 
def reducer1():
  pass

reducer()

