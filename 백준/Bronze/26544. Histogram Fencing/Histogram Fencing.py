for _ in[0]*int(input()):
    input()
    *l2,=map(int,input().split())
    *l,=map(int,input().split())
    print(sum(l2)*2+l[0]+l[-1]+sum(abs(i-j)for i,j in zip(l,l[1:])))