from Bio import SeqIO 

def loadGenome(file_genome):
	'''Loads arbitrary genome'''
	Handle = open(file_genome, "r") 
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta")) 
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def loadCi08(file_genome=f'/Users/joe/code/ref/genomes/ciona/2008/JoinedScaffold.fasta' ):
	'''Load 2008 ciona genome'''
	Handle = open(file_genome, "r") 
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta")) 
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def loadCi19(file_genome=f'/Users/joe/code/ref/genomes/ciona/2019/HT.Ref.fasta'):
	'''Load 2019 ciona genome'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def loadCi19_beta(file_genome=f'/Users/joe/code/ref/genomes/ciona/2019/HT.Ref.forBetaTesting.fasta'):
	'''Load 2019 ciona genome (for beta testing, first 1kb of each chrom)'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def loadMm10(file_genome=f'/Users/joe/code/ref/genomes/mouse/mm10/mm10.fa'):
	'''Load mm10 mouse genome'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def loadHg19(file_genome=f'/Users/joe/code/ref/genomes/human/hg19/hg19.fa'):
	'''Load hg19  genome'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def loadHg38(file_genome=f'/Users/joe/code/ref/genomes/human/hg38/hg38.fa'):
	'''Load hg38  genome'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq

def loadDr11(file_genome=f'/Users/joe/code/ref/genomes/zebrafish/danRer11/danRer11.fa'):
	'''Load Zebrafish danRer11 genome'''
	Handle = open(file_genome, "r")
	chr2seq = SeqIO.to_dict(SeqIO.parse(Handle, "fasta"))
	chr2seq = {chrom:str(chr2seq[chrom].seq).upper() for chrom in chr2seq}
	return chr2seq
