p=-1
a,b=map(int,input().split())
l=[*map(int,input().split())][::-1]
if sum(l)<b:print(len(l))
else:
    while b>=0:
        b-=l.pop()
        p+=1
    print(p)