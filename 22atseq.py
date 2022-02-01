#!/usr/bin/env python3

import random
random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# create variable for dna
# every time loop occurs, need to add an AT or GC



dna = ''

for i in range(30):
	r = random.random()
	if    r > 0.6:
		if r >0.5:
			dna += 'G'
		else: dna += 'C'
	else: 
		if r > 0.5:
			dna +='A'
		else: dna += 'T'

AT = 0
for i in range(len(dna)):
	if dna[i] == 'A': AT += 1
	elif dna[i] == 'T': AT += 1

print(len(dna),AT/len(dna), dna)
"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
