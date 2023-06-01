from collections import deque
l=[2,3,5,7]
def check_prime(n):
    for i in range(2,int(n**.5)+2):
        if n%i==0:return 0
    return 1
N=int(input())
while l:
    n=l.pop(0)
    if n>10**(N-1):
        print(n)
        continue
    for i in 1,3,7,9:
        if check_prime(n*10+i):
            l+=[n*10+i]