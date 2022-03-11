#!/usr/bin/env python3
# 61dust.py

import argparse
import mcb185 as mcb

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='masking low entropy sequence in FASTA file')

# required arguments
parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='required fasta file')
parser.add_argument('--win', required=True, type=int,
	metavar='<int>', help='required integer argument')
parser.add_argument('--ths', required=False, type=float,
	metavar='<float>', help='optional floating point argument]')
#switches
parser.add_argument('--lowercase', action='store_true',
	help='N-based masking is default, switches to lowercase masking')

# finalization
arg = parser.parse_args()

threshold = arg.ths
winsize = arg.win
file = arg.fasta
linebreak = 70

for name, seq in mcb.read_fasta(file):
	masked = ''
	for i in range(0, len(seq)-winsize+1):
		window = seq[i:i+winsize]
		if mcb.entropy(window) <= threshold:
			if arg.lowercase: masked += window.lower()
			else:             masked += 'N' * winsize
		else: masked += window
	print(name)
	for i in range(0, len(masked), linebreak): 
		print(masked[i:i+linebreak])
		

# check
# 61dust.py --fasta ../Data/chr1.fa --win 10 --ths 1 --lowercase




