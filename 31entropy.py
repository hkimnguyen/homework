#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

p = []
sum = 0
tolerance = 0.0001

for i in range(1, len(sys.argv)):
	p.append(float(sys.argv[i])) # convert to numbers
	sum += float(sys.argv[i])
	
if abs(sum - 1) > tolerance: 
	print('exceeds tolerance')
else: 
	entropy = 0 
	for x in p: entropy += -1 * (x * math.log2(x)) # -sum(pi * log(pi))
	print(sys.argv)
	print(f'{entropy:.3f}')	

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
