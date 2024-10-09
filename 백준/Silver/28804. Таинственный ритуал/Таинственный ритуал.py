d=[0,1,1,3,2,1,3,7,4,9]
n=int(input())
for _ in[0]*n:
    s=input()
    n=0
    for i in s[::-1]:
        n+=int(i)
        n=n//10+d[n%10]
    while n not in[1,3,7,9]:n=n//10+d[n%10]
    print(n)