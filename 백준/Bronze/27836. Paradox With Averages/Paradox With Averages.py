for _ in[0]*int(input()):
    input()
    c,e=map(int,input().split())
    *l1,=map(int,input().split())
    *l2,=map(int,input().split())
    s1=sum(l1)
    s2=sum(l2)
    print(sum(i*c<s1 and s2<i*e for i in l1))