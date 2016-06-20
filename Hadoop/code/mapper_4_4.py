#!/usr/bin/python
import sys
import csv
import logging
logging.basicConfig(filename="/home/training/udacity_training/code/log.log",level=logging.DEBUG)

logging.info("HI 1")
def mapper():
  reader = csv.reader(sys.stdin, delimiter="\t")
  writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
  #Skip the header line
  headers=reader.next()
  logging.info("header line is :"+str(headers))
  if headers[0]=="user_ptr_id":
    TAG="A"
  else:
    TAG="B"
  for line in reader:
     if TAG=="A":
       writer.writerow([line[0],"A",line[1],line[2],line[3],line[4]])
     else:
       writer.writerow([line[3],"B",line[0],line[1],line[2],line[5],line[6],line[7],line[8],line[9]])

#for arg in :
#  filename_in = arg
 # print "filename is "+str(filename_in)
 # sys.stdin = subprocess.Popen(["hadoop", "fs", "-cat", "myinput/"], stdout=subprocess.PIPE)
  #open(filename_in, 'r')
#logging.info("filename is : "+sys.stdin.name)
#if 'forum_users.tsv' in sys.stdin.name:
#    TAG="A"
#else:
#    TAG="B"
mapper()        
