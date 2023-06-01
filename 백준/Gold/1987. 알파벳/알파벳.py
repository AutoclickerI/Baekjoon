p,q=map(int,input().split())
l=(U:=['@'*(q+2)])+['@'+input()+'@'for _ in[0]*p]+U
V=[0]+[1]*26
V[ord(l[1][1])-64]=0
m=0
s=1
c=[0]
def X(x,y,C):
 c[0]=max(c[0],C)
 for p,q in[(1,0),(-1,0),(0,1),(0,-1)]:
  Z=ord(l[x+p][y+q])-64
  if V[Z]:V[Z]=0;X(x+p,y+q,C+1);V[Z]=1
X(1,1,1)
print(c[0])