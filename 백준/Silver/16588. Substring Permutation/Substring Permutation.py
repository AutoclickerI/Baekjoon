def c(s):
    d={}
    for i in s:d[i]=d.get(i,0)+1
    return d
a,b=map(c,open(0))
print('YNEOS'[any(a.get(k,0)<b[k]for k in b)::2])