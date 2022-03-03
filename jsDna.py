from random import choice
import itertools

Iupac2AllNt= {
        'A':['A'],
        'C':['C'],
        'G':['G'],
        'T':['T'],
        'R':['A','G'],
        'Y':['C','T'],
        'S':['G','C'],
        'W':['A','T'],
        'K':['G','T'],
        'M':['A','C'],
        'B':['C','G','T'],
        'D':['A','G','T'],
        'H':['A','C','T'],
        'V':['A','C','G'],
        'N':['A','C','G','T'],
}

ATGC=set(['A','T','G','C'])

def revcomp(dna): 
	'''Takes DNA sequence as input and returns reverse complement'''
	inv={'A':'T','T':'A','G':'C','C':'G', 'N':'N'}
	revcomp_dna=[]
	for nt in dna:
		revcomp_dna.append(inv[nt])
	return ''.join(revcomp_dna[::-1])

def count_with_revcomp(pattern,seq):    
	c=0
	for s in [seq,revcomp(seq)]:
		for kmer in get_kmers(s,len(pattern)):
			if kmer==pattern:
				c+=1
	# if pattern is palindrom, div by 2 so you dont count same twice
	if pattern==revcomp(pattern):
		return int(c/2)
	else:
		return c


def get_kmers(string,k):
	'''Takes DNA sequence as input and a kmer length and YIELDS all kmers of length K in the sequence.'''
	for i in range(len(string)):
		kmer8=string[i:i+k]
		if len(kmer8)==k:
			yield kmer8
			
def GenerateRandomDNA(length):
	'''Takes length as input and returns a random DNA string of that length.'''
	DNA=""
	for count in range(length):
		DNA+=choice("CGTA")
	return DNA

def GenerateSingleRandomSequence(template):
        '''Takes a string with letters A,T,C,G,IUPAC and returns a DNA string with rnadom AGTC nucleotides at position(s) with N.'''
        dna=''
        for i,nt in enumerate(template):
                if nt not in ATGC:
                        dna+=choice(Iupac2AllNt[nt])
                else:
                        dna+=nt
        return dna

def GenerateAllPossibleSequences(template):
	'''Takes a string with letters A,T,C,G,N and returns all possible DNA strings converting N=>A,T,G,C'''
	randomSeqList=list(itertools.product('ATGC',repeat=template.count('N')))
	seqList=set()
	for seqPossibility in randomSeqList:
		seq=seqPossibility
		dnaOut=''
		for i,nt in enumerate(template):
			if nt == 'N':
				dnaOut+=seq[0]
				seq=seq[1:]
			else:
				dnaOut+=nt
		seqList.add(dnaOut)
	return seqList

def hamming(str1, str2):
	'''Takes 2 strings as input and returns hamming distance'''
	if len(str1) != len(str2):
		raise ValueError("Strand lengths are not equal!")
	else:
		return sum(1 for (a, b) in zip(str1, str2) if a != b)

def IupacToAllPossibleSequences(dna):
	'''Takes DNA with IUPAC letters and returns all possible DNA strings with only A/G/T/C.'''
	Round2Seqs={}
	Round2Seqs[0]=[]
	for nt in Iupac2AllNt[dna[0]]:
		Round2Seqs[0].append(nt)
		
#     print(Round2Seqs)
	for i,iupac in enumerate(dna):
		if i==0: continue
			
		Round2Seqs[i]=[]
		
		for seq in Round2Seqs[i-1]:
			for nt in Iupac2AllNt[iupac]:
#                 print(nt)
#                 print(seq)
				thisSeq=seq+nt
				Round2Seqs[i].append(thisSeq)
				
	lastRound=max(Round2Seqs.keys())
	return Round2Seqs[lastRound]

def IupacToRegexPattern(dna):
	'''Takes DNA with IUPAC letters and returns a regex object that can search DNA with only A/T/G/C for the corresponding IUPAC DNA string.'''
	p=''
	for iupac in dna:
		if iupac in ['A','T','G','C']:
			p+=iupac
		else:
			p+='('
			for nt in Iupac2AllNt[iupac]:
				p+=nt
				p+='|'
			p=p[:-1]
			p+=')'
	return p

def revcomp_regex(pattern):
	'''Takes a DNA regex object and returns the reverse complement of that regex object.'''
	trans={'A':'T','G':'C','T':'A','C':'G','.':'.','(':')',')':'(','|':'|'}
	return ''.join([trans[i] for i in pattern])[::-1]

def gc_content(seq):
	'''Takes sequence as input and returns GC content from 0-1.0.'''
	return (seq.count('G')+seq.count('C'))/len(seq)
