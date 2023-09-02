n=int(input())
l=[*map(int,input().split())][::-1]
p=[0]
exec('p+=max(i+j for i,j in zip(p,l[-len(p):])),;'*n)
print(p[-1])