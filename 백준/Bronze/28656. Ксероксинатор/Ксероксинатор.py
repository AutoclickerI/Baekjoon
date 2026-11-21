_,b,*l=map(int,open(0).read().split())
s=w=0
for i in l:w+=i;s+=w;w-=min(w,b)
print(s+w)