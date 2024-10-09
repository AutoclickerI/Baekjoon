M,N=map(int,input().split())
b=eval('input(),'*M)
a=0
for _ in[0]*N:s=input();a+=any(s in i for i in b)
print(a)