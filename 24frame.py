#!/usr/bin/env python3

# Write a program that prints out the position, frame, and letter of the DNA
# Try coding this with a single loop
# Try coding this with nested loops

dna = 'ATGGCCTTT'

# single loop
for i in range(len(dna)):
	print(i, end=' ')
	if i % 3 == 2: print(2, end=' ')
	if i % 3 == 1: print(1, end=' ')
	if i % 3 == 0: print(0, end=' ')
	print(dna[i])
print()

# nested loop
for i in range(0, len(dna), 3):
	for k in range(3):
		print(i+k, k, dna[i+k])


"""
python3 24frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
