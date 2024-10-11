s=1
while n:=int(input()):
    i=[];v=n
    while v:b=input().split();i+=b;v-=len(b)
    l=sorted(zip(i,range(n)))
    print(f'Site {s}:',sum(abs(l[i][1]-i)for i in range(n)))
    s+=1   