# mcb185.py

import sys
import gzip
import math

def read_fasta(filename):
	name = None
	seqs = []

	fp = None
	if filename == '-':
		fp = sys.stdin
	elif filename.endswith('.gz'):
		fp = gzip.open(filename, 'rt')
	else:
		fp = open(filename)

	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				seq = ''.join(seqs)
				yield(name, seq)
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)
	yield(name, ''.join(seqs))
	fp.close()

# def other functions...
def letter_count(seq):
	count = {}
	for aa in seq:
		if aa not in count: count[aa] = 0
		count[aa] += 1
	return count
	
	
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


def entropy(seq):
	p = []
	
	pA = seq.count('A')/len(seq)
	pC = seq.count('C')/len(seq)
	pT = seq.count('T')/len(seq)
	pG = seq.count('G')/len(seq)
	
	if pA > 0: p.append(pA)
	if pC > 0: p.append(pC)
	if pG > 0: p.append(pG)
	if pT > 0: p.append(pT)
	
	entropy = 0
	for x in p: entropy += (-x * math.log2(x))
	return entropy



