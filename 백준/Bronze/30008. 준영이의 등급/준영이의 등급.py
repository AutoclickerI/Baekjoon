N,_,*l=map(int,open(0).read().split())
for i in l:print(sum(j<i*100//N for j in[96,89,77,60,40,23,11,4])+1)