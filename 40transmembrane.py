#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix


# reading the file
fasta = sys.argv[1]

def read_file(fasta):
	records = []
	seq = ''
	with open(fasta) as fp:
		for line in fp.readlines():
			line = line.rstrip() # removes the newline character
			if len(line) == 0: continue
			if line[0] == '>': 
				if seq != '': 
					records.append((ids, seq))
				words = line.split()
				ids = words[0][1:]
				seq = ''
			else: 
				seq += line
		records.append((ids, seq))
	return records
	

# KD calculation
def kd(peptide):
	sum = 0
	for aa in peptide:
		if   aa == 'W': sum += -0.9
		elif aa == 'C': sum +=  2.5
		elif aa == 'H': sum += -3.2
		elif aa == 'M': sum +=  1.9
		elif aa == 'Y': sum += -1.3
		elif aa == 'Q': sum += -3.5
		elif aa == 'F': sum +=  2.8
		elif aa == 'N': sum += -3.5
		elif aa == 'P': sum += -1.6
		elif aa == 'T': sum += -0.7
		elif aa == 'R': sum += -4.5
		elif aa == 'I': sum +=  4.5
		elif aa == 'D': sum += -3.5
		elif aa == 'G': sum += -0.4
		elif aa == 'A': sum +=  1.8
		elif aa == 'K': sum += -3.9
		elif aa == 'E': sum += -3.5
		elif aa == 'V': sum +=  4.2
		elif aa == 'L': sum +=  3.8
		elif aa == 'S': sum += -0.8
	return sum / len(peptide)

# print('KVLSATYGI')
	
# hydrophobic alpha-helix calculation
def ahelix(peptide, window, threshold):
	for i in range(len(peptide) - window + 1):
		pep = peptide[i:i+window]
		if 'P' in pep: continue # no prolines in alpha helix/hydrophobic regions
		if kd(pep) >= threshold: return True
	return False
	
		
# finding transmembrane proteins
for ids, seq in read_file(fasta):
	if ahelix(seq[0:30], 8, 2.5) and ahelix(seq[30:], 11, 2.0):
		print(ids)


print(sys.argv)

"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
