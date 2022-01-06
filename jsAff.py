
def loadEts(ref  =f'/Users/joe/code/ref/binding_affinity/ets/parsed_Ets1_8mers.txt'):
	'''Ets1 from mouse. Returns dictionary with key=8mer dna sequence, value=affinity (0-1.0)'''
	Seq2EtsAff  = {line.split('\t')[0]:float(line.split('\t')[1]) for line in open(ref,'r').readlines()}
	return Seq2EtsAff

def loadGata6(ref =f'/Users/joe/code/ref/binding_affinity/gata6/parsed_Gata6_3769_contig8mers.txt'):
	'''Gata6 Badis 2009'''
	Seq2GataAff = {line.split('\t')[0]:float(line.split('\t')[1]) for line in open(ref,'r').readlines()}
	return Seq2GataAff

def loadGata4(ref =f'/Users/joe/code/ref/binding_affinity/gata4/js-normalized-gata4.tsv'):  
	'''Gata4 Mariani 2017. Returns dictionary with key=8mer dna sequence, value=affinity (0-1.0)'''
	Seq2GataAff = {line.split('\t')[0]:float(line.split('\t')[1]) for line in open(ref,'r').readlines()}
	return Seq2GataAff

def loadTbx(ref=f'/Users/joe/code/ref/binding_affinity/tbx5/mariani-et-al-2017/js-normalized-tbx5-mariani2017.tsv'):
	'''Tbx5 Mariani 2017. Returns dictionary with key=8mer dna sequence, value=affinity (0-1.0)'''
	Seq2TbxAff = {line.split('\t')[0]:float(line.split('\t')[1]) for line in open(ref,'r').readlines()}
	return Seq2TbxAff

def loadNkx(ref=f'/Users/joe/code/ref/binding_affinity/nkx2-5/js-normalized-nkx25.tsv'):
	'''Nkx2 Barerra 2016. Returns dictionary with key=8mer dna sequence, value=affinity (0-1.0)'''
	Seq2NkxAff = {line.split('\t')[0]:float(line.split('\t')[1]) for line in open(ref,'r').readlines()}
	return Seq2NkxAff

def loadAr(ref=f'/Users/joe/code/ref/binding_affinity/ar/js-normalized-ar-8mer-affinities.tsv'):
	'''Ar. Returns dictionary with key=8mer dna sequence, value=affinity (0-1.0)'''
	Seq2ArAff = {line.split('\t')[0]:float(line.split('\t')[2]) for line in open(ref,'r').readlines()}
	return Seq2ArAff
