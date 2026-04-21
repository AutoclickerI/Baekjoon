d={}
for s in[*open(0)][1:]:
    s=s[:-1]
    if i:=d.get(s):
        while(t:=s+str(i))in d:i+=1
        d[s]=i+1;s=t
    print(s)
    d[s]=1