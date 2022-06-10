from Bio import SeqIO
import gzip
import jsDna as jsd

def linker_parse(seq,linker,max_hamming_dist,pos):
    
    linkerLen=len(linker)    
    putativeLinker=seq[pos:pos+linkerLen]
    
    if putativeLinker==linker:
        return seq.split(linker)
    else:
        d=jsd.hamming(putativeLinker,linker)
        if d<=max_hamming_dist:
            return seq.split(putativeLinker)

def linker_parse_pos(seq,linker,pos,max_right,max_left,max_hamming_dist):
    '''Parses sequence using a linker. First start looks at pos. Allows 
for mismatches up to max_hamming_dist. Then looks left/right until you 
reach max_right and max_left. If you look max_right=1 and max_left=2 you 
will look at 29,30,31,32'''
    
    #######################################
    # Check if at expected location
    #######################################
    
    result=linker_parse(seq,linker,max_hamming_dist,pos)
    if result: return result
    else:      pass
        
    #######################################
    # Check at +/- loc
    #######################################
    
    for posi in range(pos-max_left-1,pos+max_right):
        result=linker_parse(seq,linker,max_hamming_dist,posi)
        if result: return result
        else:      continue
        
    return False


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
