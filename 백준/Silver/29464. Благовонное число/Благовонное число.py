import sys
sys.setrecursionlimit(10**5)
n=int(input())
i=0
x=0
while x+(i and 9*10**((i-1)//2))<n:
    x+=(i and 9*10**((i-1)//2))
    i+=1
def recur(i,n,c=1):
    if i==1:return str(n-1+c)
    if i==2:return str(n-1+c)*2
    while 10**((i-1)//2)<n:
        c+=1
        n-=10**((i-1)//2)
    return f'{c}{recur(i-2,n,0)}{c}'
print(recur(i,n-x))