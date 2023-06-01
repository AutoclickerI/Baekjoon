for i in[*open(0)][1:]:
 p,q,r=map(int,i.replace(*'/.').split('.'))
 if'/'in i:p,q=q,p
 print(f'{p:02d}.{q:02d}.{r:04d}',f'{q:02d}/{p:02d}/{r:04d}')