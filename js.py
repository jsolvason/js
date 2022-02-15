import os
import datetime

def flatten_list(l):
    return [i for sublist in l for i in sublist]


def replace_chars_with_null(string,charList):
    for c in charList:
        string=string.replace(c,'')
    return string

def get_todays_datestring(format="%Y%m%d"):
    dateString=datetime.date.today().strftime(format)
    return dateString

def get_basename(fn):
    return fn.split('/')[-1].split('.')[0]

def listModules():
    lsResult=os.popen("ls /Users/joe/pybin/js/js*.py").read().split('\n')
    lsResult=[i.split('/')[-1] for i in lsResult]
    for i in lsResult: print(i)

def mkdir_if_dir_not_exists(out_dir):
    if not os.path.exists(out_dir): os.mkdir(out_dir)

def basename(fn):
    return fn.split('/')[-1].split('.')[0]

def percent(number,rounding_digit=1):
    if rounding_digit==0:
        return str(int(100*number))+' %'
    else:
        return str(round(100*number,rounding_digit))+' %'                                             

def million(number):
    return str(round(number/1e6,2))+ ' mil'

def write_row(rowList,delim='\t'):
    return delim.join([str(i) for i in rowList])+'\n'

def strjoin(delim,l):
    return delim.join([str(i) for i in l])

def read_tsv(fn,pc,header,breakBool=False,sep='\t',pc_list=False):
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

def dprint(d,n):
    for i,(k,v) in enumerate(d.items()):
        if i<=n:
            print(k,v)
