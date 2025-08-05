_,*l=map(int,open(0))
while l:
 s=[0]*1001;n,*l=l
 for i in l[:n]:s[i]+=1
 print(s.index(max(s)));l=l[n:]