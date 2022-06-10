etsCores=set(['GGAA','GGAT','TTCC','ATCC'])
gataCores=set(['GATA','TATC'])

def loadAff(ref):
        '''Load an arbitrary affinity dataset. First column should be 8mer DNA 
sequence and second column should be the normalized affinity (between 0-1).'''
        Seq2EtsAff  = {line.split('\t')[0]:float(line.split('\t')[1]) for line in open(ref,'r').readlines()}
        return Seq2EtsAff

