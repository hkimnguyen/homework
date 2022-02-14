#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

num = []
for i in range(1, len(sys.argv)): 
	num.append(float(sys.argv[i])) # need to make them actual numbers instead of text


# finding count and minimum
num.sort()
count = len(num)
min = num[0] # smallest value at num[0] bc sorted the list

# finding maximum and mean
sum = num[0]
for k in range(1, count):
	if num[k] > min: max = num[k] # loop compares values in list to min to find max
	sum += num[k]
mean = sum/count

# finding median
if count % 2 == 0: # even numbered count
	med1 = num[count // 2]
	med2 = num[(count // 2)-1]
	med = (med1 + med2)/2
else: med = num[math.floor(count/2)] # odd numbered count


# finding std deviation
varsum = 0
for j in range(0, count):
	diff = num[j] - mean # find variance first
	varsum += (diff ** 2)
	var = varsum/(count) # for population std dev; use (count - 1) for sample ?
	std = var ** 0.5


print(sys.argv)
print('Count:', count)
print('Minimum:', min)
print('Maximum:', max)
print('Mean:', f'{mean:.3f}')
print('Std. dev:', f'{std:.3f}')
print('Median:', f'{med:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
