I=lambda:map(int,input().split())
for i in range(*I()):
  n,v=I();a=0;d=0,*[[*I()]for _ in[0]*n]
  for _ in[0]*v:p,q,r=I();a+=d[p][1]*(d[p][0]or r==1)+d[q][1]*(d[q][0]or 1<r)
  print(f'Data Set {i+1}:\n{a}\n')