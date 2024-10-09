d=[0,1,1,3,2,1,3,7,4,9]
for s in[*open(0)][1:]:
    n=0
    for i in s[-2::-1]:n+=int(i);n=n//10+d[n%10]
    while n in[2,4,5,6,8]:n=n//10+d[n%10]
    print(n)