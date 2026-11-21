n,l,_,*L=open(0)
n=int(n)
*l,=map(int,l.split())
b=[[0]*n for _ in[0]*n]
for i in range(n-1):
 j=J=1
 while 2*j-1<i+j<len(l)and l[i-j]==l[i+j]:b[i-j][i+j]=1;j+=1
 while 2*J-2<i+J<len(l)and l[i-J+1]==l[i+J]:b[i-J+1][i+J]=1;J+=1
for i in L:p,q=map(int,i.split());print(+(p==q)or b[p-1][q-1])