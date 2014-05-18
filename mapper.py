#!/usr/bin/python

# Format of each line is:
# date\ttime\tstore name\titem description\tcost\tmethod of payment
#
# We want elements 2 (store name) and 4 (cost)
# We need to write them out to standard output, separated by a tab

import sys

def mapper():
	#read standard input line by line
	for line in sys.stdin:
		#strip off extra whiltespace, split by tab and put then in array	
		data=line.strip().split("\t")
		if len(data) == 6
			#this is multiple assignment, it assigns data[0] to date, data[1] to time and so on
			date, time, store, item, cost, payment = data
			print "{0}\t{1}".format(store,cost)
