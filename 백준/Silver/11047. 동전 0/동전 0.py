a,b=list(map(int,input().split()))
c=[int(input())for i in range(a)]
n=0
while b>0:
    l=c.pop()
    while b>=l:
        b-=l
        n+=1
print(n)