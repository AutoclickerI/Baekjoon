s=sorted
for i in[*open(0)][1:]:
 A,B=s(map(int,i.split()))
 while A-B:A,B=s([A,B>>1])
 print(10*A)