i=0
while n:=int(input()):
    l=eval('input(),'*n);r=set()
    for _ in range(2*n-1):r^={int(input().split()[0])}
    print(i:=i+1,l[r.pop()-1])