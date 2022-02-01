#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'

for nt in dna[::-1]:
	if   nt == 'A': print('T', end='')
	elif nt == 'T': print('A', end='')
	elif nt == 'G': print('C', end='')
	else:           print('G', end='')


"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
