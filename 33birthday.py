#!/usr/bin/env python3

# You are probably well aware of the 'birthday paradox'
# https://en.wikipedia.org/wiki/Birthday_problem
# Let's try simulating it

# You will need a list for the 365 day calendar
# You will need a set number of people (e.g. 25)
# During each 'trial' you do the following
#	Choose a person
#	Git them a random birthday
#	Store it in the calendar
# Once you have stored all birthdays, check to see if any have the same day
# Do this for many trials to see what the probability of sharing a birthday is

import random

days = 365
people = 23
trials = 10000
shared = 0

for k in range(trials): 
	calendar = [0] * days
	for i in range(people):
		birthday = random.randint(0, days - 1)
		calendar[birthday] += 1
	# print(calendar)	
	collision = False #flag to check collisions
	for v in calendar: 
		if v > 1: # only need one collision to include in probability
			collision = True
	if collision: shared += 1
		
print(shared/trials)


"""
python3 33birthday.py
0.571
"""

