*l,=map(int,input().split())
arr=[-1]*10
for i in range(10):arr[l[i]]=i
fa,fb=input().split()
A=int(''.join(str(arr[int(i)])for i in fa))
B=int(''.join(str(arr[int(i)])for i in fb))
x=str(A+B)
print(*[l[int(i)]for i in str(x)],sep='')