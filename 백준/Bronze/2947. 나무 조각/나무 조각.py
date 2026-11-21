l=input().split()
while l!=sorted(l):
    for i in range(4):
        if l[i+1]<l[i]:
            l[i:i+2]=l[i+1],l[i]
            print(*l)