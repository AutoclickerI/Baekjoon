for i in[*open(0)][1:]:
 A,B=sorted(map(int,i.split()))
 while A-B:A,B=sorted([A,B>>1])
 print(10*A)