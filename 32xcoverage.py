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


coverage = []

for i in range(genome):
	coverage.append(0)
	
# assigning random read positions in genome
for i in range(readnum):
	r = random.randint(0, genome - readlen + 1)
	for j in range(r, r+readlen - 1):
		coverage[j] += 1
	
sum = 0
min = readnum # setting to some value that is higher than actual min
max = 0 # bc max should be greater than 0
for x in coverage:
	sum += x
	if x == 0: continue
	if x < min: min = x
	if x > max: max = x
average = sum/len(coverage)

	
print(sys.argv)
print(min, max, average)


# worked with Keith in OH


# min/max by sorting first
# sorted_genome = coverage[readlen:genome-readlen]
# sorted_genome.sort()
# min = sorted_genome[0]
# max = sorted_genome[-1]




"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""