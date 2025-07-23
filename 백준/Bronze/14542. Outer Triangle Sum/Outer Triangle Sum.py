T=0
while n:=int(input()):
    T+=1
    l=eval('input().split(),'*n)
    print(f'Case #{T}:{sum(int(i[0])+int(i[-1])for i in l)-int(l[0][0])+sum(map(int,l[-1][1:-1]or[0]))}')