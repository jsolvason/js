from Bio import SeqIO 
from pyliftover import LiftOver
import pickle
import pandas as pd
import js

def getLiftoverObject(startGenome,endGenome):
    '''A method to create a liftover object for jsg.liftover()'''
    return LiftOver(startGenome, endGenome)

def liftover(liftOverObject,c,s):
    strloResults = liftOverObject.convert_coordinate(c,s)
    if (strloResults==[]): return False
    else:
        hg38chrom,hg38pos,strand,score=strloResults[0]
        if c!=hg38chrom:     return 'Chrom1≠Chrom2'
        else:                return hg38chrom,hg38pos

def liftover_interval(liftOverObject,c,s,e):
    '''A method to liftover coordinates from previous to current genome. requires pyliftover'''
    strloResults = liftOverObject.convert_coordinate(c,s)
    endloResults   = liftOverObject.convert_coordinate(c,e)

    # If fail
    if (strloResults==[]) or (endloResults==[]):
        return False

    # If correct
    else:
        hg38chrom,hg38s,strand,score=strloResults[0]
        hg38chrom,hg38e,strand,score=endloResults[0]

        if hg38s>hg38e: 
            return 'S>E'

        if c!=hg38chrom:
            return 'Chrom1≠Chrom2'

        else:
            return hg38chrom,hg38s,hg38e

def liftover_interval_batch(in_bed,loObject):
    '''A method to liftover intervals (chrom,start,end) from an entire bed file'''

    line_out=''
    n=0
    fail_list=[]
    for row in js.read_tsv(in_bed,pc=False,header=False):
        n+=1
        
        chrom,start,end=row
        start,end=int(start),int(end)

        lo=liftover_interval(loObject,chrom,start,end)
        
        # If lo fails
        if lo==False or type(lo)==str:         
            fail_list.append(lo)
        
        # if low success
        else:             
            newChrom,newStart,newEnd=lo
            line_out+=js.write_row([newChrom,newStart,newEnd])
    
    errors=100 * pd.Series(fail_list).value_counts() / n
    
    return line_out,errors

def parse_cse(cse):
    '''A method to convert genome broser coords (ie chr1:1,000,000-1,200,000) to python variables.'''
    c,se=cse.split(':')
    s,e=[int(i.replace(',','')) for i in se.split('-')]
    return c,s,e

def faLoadGenome(file_genome):
	'''Loads arbitrary genome'''
	Handle = open(file_genome, "r") 
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta")) 
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def faLoadGenome(pickled_file_genome):
	'''Loads arbitrary genome'''
	with open(pickled_file_genome,'rb') as f:
		chr2seq=pickle.load(f)
	return chr2seq

def pklLoadHg38(pickled_file_genome=f'/Users/joe/code/ref/genomes/human/hg38/hg38.fa.chr2seq.pydict.pickle'):
	'''Loads arbitrary genome'''
	with open(pickled_file_genome,'rb') as f:
		chr2seq=pickle.load(f)
	return chr2seq

def pklLoadHg19(pickled_file_genome=f'/Users/joe/code/ref/genomes/human/hg19/hg19.fa.chr2seq.pydict.pickle'):
	'''Loads arbitrary genome'''
	with open(pickled_file_genome,'rb') as f:
		chr2seq=pickle.load(f)
	return chr2seq

def faLoadCi08(file_genome=f'/Users/joe/code/ref/genomes/ciona/2008/JoinedScaffold.fasta' ):
	'''Load 2008 ciona genome'''
	Handle = open(file_genome, "r") 
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta")) 
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def faLoadCi19(file_genome=f'/Users/joe/code/ref/genomes/ciona/2019/HT.Ref.fasta'):
	'''Load 2019 ciona genome'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def faLoadCi19_beta(file_genome=f'/Users/joe/code/ref/genomes/ciona/2019/HT.Ref.forBetaTesting.fasta'):
	'''Load 2019 ciona genome (for beta testing, first 1kb of each chrom)'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def faLoadMm10(file_genome=f'/Users/joe/code/ref/genomes/mouse/mm10/mm10.fa'):
	'''Load mm10 mouse genome'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def faLoadHg19(file_genome=f'/Users/joe/code/ref/genomes/human/hg19/hg19.fa'):
	'''Load hg19  genome'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def faLoadHg38(file_genome=f'/Users/joe/code/ref/genomes/human/hg38/hg38.fa'):
	'''Load hg38  genome'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def faLoadDr11(file_genome=f'/Users/joe/code/ref/genomes/zebrafish/danRer11/danRer11.fa'):
	'''Load Zebrafish danRer11 genome'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq
