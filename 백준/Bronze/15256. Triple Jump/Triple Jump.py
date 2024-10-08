for s in[*open(i:=0)][2::2]:
 *v,=map(eval,s.split())
 for j,x in enumerate(v):
  if 30<=x<=30.2:break
 i+=1;print(f'Data Set {i}: {min(v[j+3:]or[30])-30:.2f}\n')