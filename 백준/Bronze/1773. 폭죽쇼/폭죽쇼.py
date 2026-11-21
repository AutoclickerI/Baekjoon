_,n,*l=map(int,open(0).read().split())
a=[0]*-~n
for i in l:a[i::i]=n//i*[1]
print(sum(a))