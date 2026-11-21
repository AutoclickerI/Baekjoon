n=int(input())
*l,=map(int,input().split())
s=1
L1=[1]
for i,j in zip(l,l[1:]):
    if i<j:L1+=[L1[-1]+1]
    if i==j:L1+=[L1[-1]]
    if i>j:L1+=[1]
L2=[1]
for i,j in zip(l[::-1],l[-2::-1]):
    if i<j:L2+=[L2[-1]+1]
    if i==j:L2+=[L2[-1]]
    if i>j:L2+=[1]
print(max(L1+L2))