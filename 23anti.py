#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'[:: -1]

for i in range(len(dna)):
	if   dna[i] == 'A': print('T', end='')
	elif dna[i] == 'T': print('A', end='')
	elif dna[i] == 'G': print('C', end='')
	else:               print('G', end='')
print() 
"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
