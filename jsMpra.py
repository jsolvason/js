from Bio import SeqIO
import gzip
import jsDna as jsd

def read_fastq(fn,is_gzip=False,get_quality=False,print_progress=False):
    
    if gzip: open_func=gzip.open(fn,'rt')
    else:    open_func=open(fn,'r')
        
    with open_func as handle:
        
        for record in SeqIO.parse(handle, "fastq"):
                
            qualityList=record.letter_annotations["phred_quality"]
            seq=str(record.seq)

            if get_quality:
                yield seq,qualityList
            else:
                yield seq

esp3i='CGTCTC'
bbsi='GAAGAC'
sbfi='CCTGCAGG'

def returnEnzymeCounts_withRevcomp(seq_with_synthesisAdapters,restrictionEnzymes=[esp3i,bbsi,sbfi]):
    '''A method to determine how many re sites in each library member sequence ordered (also considers revcomp). Returns the counts of enzymes provided'''
    
    # Check both seqs
    seqCounts=[] # should = [2,0,0] for sequences without extra enzyme site

    for pattern in restrictionEnzymes:
        count=jsd.count_with_revcomp(pattern,seq_with_synthesisAdapters)
        seqCounts.append(count)
    seqCounts=tuple(seqCounts)
    
    return seqCounts 

def normalize_minmax_list(l):
    '''A method to do min max scaling for library. 
    Note: 1) Returns np.NaN values when str(value)=='nan'
          2) Doesnt use np.NaN values to determine max/min'''
    # remove na entries
    l_for_min_max=[i for i in l if str(i)!='nan']
    
    MIN=min(l_for_min_max)
    MAX=max(l_for_min_max)
    
    out=[]
    for i in l:
        if str(i)!='nan': out.append((i-MIN) / (MAX-MIN))
        else:             out.append(np.NaN)
    return out

def normalize_minmax(i,MIN,MAX):
    '''A method to do min max scaling of a measuremnet i against its min/max.'''
    return (i-MIN) / (MAX-MIN)
