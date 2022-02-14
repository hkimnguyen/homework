#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

genome  = int(sys.argv[1]) # size of genome in bp
readnum = int(sys.argv[2]) # number of reads
readlen = int(sys.argv[3]) # read length in bp
coverage = [0] * genome


	
for i in range(readnum):
	r = random.randint(0, genome)
	read = coverage[r:r+readlen]
	for j, reads in enumerate(read):
		coverage[j] += 1
	print(coverage)


sum = 0 # total numbers of bp read
# average = sum/(readnum * readlen)
	
print(sys.argv)






"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""