def normalize_minmax(l):
    
    # remove na entries
    l_for_min_max=[i for i in l if str(i)!='nan']
    
    MIN=min(l_for_min_max)
    MAX=max(l_for_min_max)
    
    out=[]
    for i in l:
        if str(i)!='nan': out.append((i-MIN) / (MAX-MIN))
        else:             out.append(np.NaN)
    return out
