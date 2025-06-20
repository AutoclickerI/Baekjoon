def f(a,b):
    if a==b:
        return 0,0
    if(a,b)==(1,2):
        return 6,0
    if(a,b)==(2,1):
        return 0,6
    if a-b==1:
        return 0,a+b
    if b-a==1:
        return a+b,0
    if a<b:
        return 0,b
    return a,0
while'0'<input():
    A,B=zip(*map(f,map(int,input().split()),map(int,input().split())))
    print('A has',sum(A),'points. B has',sum(B),'points.\n')