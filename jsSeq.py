from Bio import SeqIO
import gzip
import jsDna as jsd

def read_fastq(fn,is_gzip=False,get_quality=False,print_progress=False):
    
    if is_gzip: open_func=gzip.open(fn,'rt')
    else:    open_func=open(fn,'r')
        
    with open_func as handle:
        
        for record in SeqIO.parse(handle, "fastq"):
                
            qualityList=record.letter_annotations["phred_quality"]
            seq=str(record.seq)

            if get_quality:
                yield seq,qualityList
            else:
                yield seq

def read_fasta(fn,is_gzip=False):
    
    if is_gzip: open_func=gzip.open(fn,'rt')
    else:       open_func=open(fn,'r')

    with open(fn,'r') as handle:
        for record in SeqIO.parse(handle, "fasta"):
            yield record.id, record.seq.upper()
