h=-1e9
n=0
for s,c in sorted([[-int(i)*10-sum(sorted(map(int,j))[1:5]),c]for c,i,*j in map(str.split,[*open(0)][1:])],key=lambda s:s[0]):
    n+=1
    if s>h:
        h=s
        if n>3:break
    print(c,-s)