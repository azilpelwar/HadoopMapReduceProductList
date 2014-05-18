#!/usr/bin/python

# We are using the Hadoop streaming for communicating to the Hadoop engine
# Hadoop streaming allows Hadoop to communicate with any language 
# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store

import sys
def reducer():
	salesTotal=0
	oldKey=None
	for line in sys.stdin:
		data=line.strip.split("\t")
		if len(data) != 2:
			continue
		thisKey, thisSale = data
		if oldKey and oldKey!=thiKey:
			print "{0}\t{1}".format(oldKey,salesTotal)
			salesTotal=0
		oldKey=thisKey
		salesTotal += float(thisSale)
	#Finally print result for Last store from the DB
	if oldKey!=None:
		print "{0}\t{1}".format(oldKey,salesTotal)
