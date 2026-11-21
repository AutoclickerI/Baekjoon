t=36
*l,=map(int,open(s:=0).read().split())
for i in l[:6]:
  for j in l[6:]:s+=i>j;t-=i==j
print(f'{s/t:.5f}')