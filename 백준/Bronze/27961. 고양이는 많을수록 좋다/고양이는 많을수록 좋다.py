N=int(input())
n=0
while 2**n<N:n+=1
print(n+1 if N else 0)