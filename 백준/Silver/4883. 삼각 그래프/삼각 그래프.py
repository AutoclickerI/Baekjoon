T=0
while n:=int(input()):
    T+=1
    *t,=map(int,input().split())
    t[2]+=t[1]
    t[0]=float('inf')
    for _ in[0]*~-n:
        a,b,c=map(int,input().split())
        t=[min(t[:2])+a,min(t)+b,min(t[1:])+c]
        t[1]=min(t[1],t[0]+b)
        t[2]=min(t[2],t[1]+c)
    print('%d.'%T,t[1])