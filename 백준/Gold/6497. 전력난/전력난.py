while(l:=input())>'00':exec('''
p,q=map(int,l.split())
P=[*range(p)]
A=0
def F(n):
 if P[n]-n:P[n]=F(P[n])
 return P[n]
S=sorted
l=[[*map(int,input().split())]for _ in[0]*q]
s=sum(i[2] for i in l)
for a,b,c in S(l,key=lambda l:l[2]):
 a,b=S([F(a),F(b)])
 if a-b:A+=c;P[b]=a
print(s-A)''')