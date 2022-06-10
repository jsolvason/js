import os
import datetime
import pandas as pd
import time

import time

def time_iter_progress(lc,n,timestart,end='\n'):
    '''Time processing or analysis progress.'''
    
    timenow=time.time()
    minElapsed=(timenow-timestart)/60
    lcPerMin=lc/minElapsed
    
    lcRemain=n-lc
    minRemain=lcRemain/lcPerMin
    
    print(f'{js.percent(lc/n)} complete ({round(minRemain,1)} min remain)')


def text2md5(md5fn,parse_type):
    '''Create md52fn pydict for ensuring md5sums are correct.'''
    if parse_type  not in ['linux','mac']: raise ValueError('parse_type not supported')
    
    if parse_type=='linux':
        md52fn={}
        for row in read_tsv(md5fn,pc=False,header=False):
            line=row[0]
            md5,fn=line.split('  ')
            fn=fn.split('/')[-1]
            
            md52fn[md5]=fn
            
    elif parse_type=='mac':
        md52fn={}
        for row in read_tsv(md5fn,pc=False,header=False):
            line=row[0]
            line=line.replace('MD5 (','').replace(')','')
            fn,md5=line.split(' = ')
            fn=fn.split('/')[-1 ]
            
            md52fn[md5]=fn
            
    return md52fn

def md5_comparison(md52fn1,title1,md52fn2,title2):
    '''Compare md5s of files at two locations to ensure successful datatransfer'''

    fn2md51={v:k for k,v in md52fn1.items()}
    fn2md52={v:k for k,v in md52fn2.items()}
    
    fnSet1=set(fn2md51.keys())
    fnSet2=set(fn2md52.keys())
    
    print( '####################')
    print( '# Md5 Names         ')
    print(f'1: {title1}         ')
    print(f'2: {title2}       \n')
    
    # determine if which filenames are specific to one location
    print( '########################')
    print( '# Unique Files')
    print(f'Files unique to {title1}')
    print(fnSet1-fnSet2              )
    print(                           )
    print(f'Files unique to {title2}')
    print(fnSet2-fnSet1              )
    print(                           )
    
    ################################################################
    # Determine if changes to file names
    ################################################################
    
    fileNameChange=False
    md52fns={}
    md52fntitle={}
    for md52fn,title in [(md52fn1,title1),(md52fn2,title2)]:
        for md5,fn in md52fn.items():
            if md5 not in md52fns: 
                md52fns[md5]=set()
                md52fntitle[md5]=set()
            md52fntitle[md5].add((title,fn))    
            md52fns[md5].add(fn)

    print( '#########################    ')
    print( '# Changes to file names?   \n')
    for md5,fnSet in md52fns.items():
        if len(fnSet)>1:
            fileNameChange=True
            print(    f'!!! >> {md5} maps to...')
            for fn in fnSet:
                print(f'                       >> {fn} ')
                
        elif len(fnSet)==1:
            fn=list(fnSet)[0]
            print(    f' ok >> {md5} >> {fn}')
    
    if fileNameChange: print('\n==> ≥1 File Name Change Detected')
    
    ################################################################
    # Determine if corruption in data
    ################################################################
    
    fileCorruption=False
    fn2md5s={}
    fn2md5title={}
    for fn2md5,title in [(fn2md51,title1),(fn2md52,title2)]:
        for fn,md5 in fn2md5.items():
            if fn not in fn2md5s: 
                fn2md5s[fn]=set()
                fn2md5title[fn]=set()
            fn2md5title[fn].add((title,md5))    
            fn2md5s[fn].add(md5)

    print('\n\n\n')
    print( '#########################    ')
    print( '# Corruption in data?      \n')
    for fn,md5Set in fn2md5s.items():
        if len(md5Set)>1:
            fileCorruption=True
            print(    f'!!! >> {fn} maps to...')
            for title,md5 in fn2md5title[fn]:
                print(f'                       >> {md5} {title} ')
                
        elif len(md5Set)==1:
            md5=list(md5Set)[0]
            print(    f' ok >> {fn} >> {md5}')
            
    if fileCorruption: print('\n==> ≥1 File Corrupted')
    else: print('\n==> All Files OK')

def md5_comparison_from_filenames(fn1,parsetype1,title1,fn2,parsetype2,title2):
    '''Wrapper function to simply plug in two md5.txt files and compare md5 sums'''
    md52fn1=text2md5(fn1,parsetype1)
    md52fn2=text2md5(fn2,parsetype2)
    md5_comparison(md52fn1,title1,md52fn2,title2)

    
def tsv_to_excel(inTsv,outExcel=''):
    '''Convert a .tsv to .xlsx'''
    
    # Create default name if no name given
    if outExcel=='': outExcel=inTsv+'.xlsx'
    
    # ensure suffix is correctr 
    if '.xlsx' not in outExcel: raise ValueError('Name must end in .xlsx')
    
    df=pd.read_csv(inTsv,sep='\t')
    df.to_excel(outExcel,index=None,header=None)

def flatten_list(l):
    '''Returns [1,2,3,4] for inputted [[1,2],[3,4]]'''
    return [i for sublist in l for i in sublist]


def replace_chars_with_null(string,charList):
    '''Deletes all input characters in string'''
    for c in charList:
        string=string.replace(c,'')
    return string

def get_todays_datestring(format="%Y%m%d"):
    '''Get todays date as string formatted YYYYMMDD'''
    dateString=datetime.date.today().strftime(format)
    return dateString

def get_basename(fn):
    '''Get basename of file. e.g. /path/to/file.suff1.txt => file'''
    return fn.split('/')[-1].split('.')[0]

def mkdir_if_dir_not_exists(out_dir):
    '''Make a directory only if that directory doesnt exist'''
    if not os.path.exists(out_dir): os.mkdir(out_dir)

def percent(number,rounding_digit=1):
    '''Get percent of fraction'''
    if rounding_digit==0:
        return str(int(100*number))+'%'
    else:
        return str(round(100*number,rounding_digit))+'%'                                             

def million(number):
    '''Get number in terms of million'''
    return str(round(number/1e6,2))+ ' mil'

def write_row(rowList,delim='\t'):
    '''Write a single row of a tsv file.'''
    return delim.join([str(i) for i in rowList])+'\n'

def strjoin(delim,l):
    '''Join items in a list into a string'''
    return delim.join([str(i) for i in l])

def read_tsv(fn,pc,header,breakBool=False,sep='\t',pc_list=False):
    '''Read a tsv file'''
    with open(fn,'r') as f:
        
        # If printing columns, skip header
        if header:
            if (pc==True): pass
            else:          next(f)
                
        for i,line in enumerate(f):
            a=line.strip().split(sep)
            if pc:
                if pc_list==False:
                    if i==0:
                        for i,c in enumerate(a):
                            print(i,c)
                        print()
                        if breakBool: break
                        continue
                else:
                    if i==0:
                        print(', '.join([i.replace('-','_').replace(' ','_') for i in a]))
                        if breakBool: break
                        continue
            yield a

def dprint(d,n=0):
    '''Print a dictionary'''
    for i,(k,v) in enumerate(d.items()):
        if i<=n:
            print(k,v)
