_,*l=open(0)
while l:
 a,b,c,*l=l;d=[1]+[0]*6**6
 for i in map(int,b.split()):
  for j in range(5**6):d[j]+=d[j-i]
 print(d[int(c)])