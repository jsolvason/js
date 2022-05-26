from Bio import SeqIO 
from pyliftover import LiftOver
import pickle
import pandas as pd
import js

def generate_Chrom2NumStartEnd(chr2seq):
    '''Generates obj for choose_random_chrom_pos()'''
    Chrom2NumStartEnd={}  
    n=0
    for chrom,seq in chr2seq.items():
        begin=n
        end=begin+len(seq)
        Chrom2NumStartEnd[chrom]=(begin,end)
        n=end
    return genomeLen,Chrom2NumStartEnd

def choose_random_chrom_pos(genomeLen,Chrom2NumStartEnd):
    n=np.random.randint(genomeLen)
    for chrom,(start,end) in Chrom2NumStartEnd.items():
        if n>= start and n<=end:
            return chrom,n-start

def getLiftoverObject(startGenome,endGenome):
    '''A method to create a liftover object for jsg.liftover()'''
    return LiftOver(startGenome, endGenome)

def liftover_pos(liftOverObject,c,s):
    '''A method to liftover a single chrom/pos pair'''
    strloResults = liftOverObject.convert_coordinate(c,s)
    if (strloResults==[]): return False,'NotFound'
    if (strloResults==None): return False,'NotFound'
    else:
        hg38chrom,hg38pos,strand,score=strloResults[0]
        if c!=hg38chrom:     
            return False,'ChrOld≠ChrNew'
        else:                
            return hg38chrom,hg38pos

def liftover_start_end(liftOverObject,c,s,e):
    '''A method to liftover a chrom/start/end.'''
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

def liftover_interval_batch(in_bed,loObject,out_bed):
    '''A method to liftover intervals (chrom,start,end) from an entire bed file'''

    line_out=''
    n=0
    fail_list=[]
    warning_interval_flip=0
    #NewCoord2OldCoord={}
    for row in js.read_tsv(in_bed,pc=False,header=False):
        n+=1
        
        chrom,start,end=row
        start,end=int(start),int(end)
        #if (chrom,start,end) in NewCoord2OldCoord: raise ValueError('Duplicate region detected')

        lo=liftover_start_end(loObject,chrom,start,end)
        
        # If lo fails
        if lo==False or type(lo)==str:         
            fail_list.append(lo)
        
        # if lo success
        else:             
            newChrom,newStart,newEnd=lo
            if newStart<newEnd: 
                line_out+=js.write_row([newChrom,newStart,newEnd])
                #NewCoord2OldCoord[(chrom,start,end)]=(newChrom,newStart,newEnd)
            else:
                line_out+=js.write_row([newChrom,newEnd,newStart])
                #NewCoord2OldCoord[(chrom,start,end)]=(newChrom,newEnd,newStart)
                warning_interval_flip+=1
    
    errors=100 * pd.Series(fail_list).value_counts() / n
    
    if warning_interval_flip>0:
        print(f'Warning: {warning_interval_flip} intervals had start>end')
    print('Percent of error cases:')
    print(errors)

    with open(out_bed,'w') as f: f.write(line_out)
    #with open(out_bed+'.new2old.pydict.pickle','wb') as f: pickle.dump(NewCoord2OldCoord,f,protocol=pickle.HIGHEST_PROTOCOL)

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

def pklLoadGenome(pickled_file_genome):
	'''Loads arbitrary genome'''
	with open(pickled_file_genome,'rb') as f:
		chr2seq=pickle.load(f)
	return chr2seq

