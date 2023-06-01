I=input
for i in range(int(I())):
 n=int(I())
 *l,=map(int,I().split())
 for j in range(1,n-1):l[j]=min(l[j-1]+l[j+1],2*l[j])/2
 print(f'Case #{i+1}:',l[-2])