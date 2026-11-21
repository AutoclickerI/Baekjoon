for s in[*open(0)][1:]:
 n=len(s)-1;v=[1]*n;i=0
 for c in s[:n]:
  for j in range(max(0,i-(c!='D')-(c<'C')),min(n,i-~(c>'R'))):v[j]&=c<'A'
  i+=1
 print(sum(v))