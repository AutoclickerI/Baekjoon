m,*_,M=sorted(l:=[*map(int,[*open(0)][1].split())])
for i in l:print(max(M-i,i-m))