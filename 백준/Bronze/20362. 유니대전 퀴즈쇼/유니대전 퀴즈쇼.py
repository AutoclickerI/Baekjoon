n,c,*l=open(0).read().split()
s=l[::2].index(c)*2+1
print(sum(i==l[s]for i in l[1:s:2]))