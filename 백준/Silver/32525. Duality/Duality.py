i=open(0)
input=lambda:next(i)
for T in[0]*int(input()):
    for _ in[0]*int(input()):T+=1;x,y=map(int,input().split());print(T,x+5*10**8,y+1)