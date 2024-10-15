for T in range(int(input())):
    n,m=input().split();k=[[eval(m)]];v=h=0
    for x,y,z in eval('map(eval,input().split()),'*int(n))[::-1]:k+=[x+k[-1][0],y,z],
    for m,t,f in k[:0:-1]:a=f/m-9.81;h+=v*t+a*t*t/2;v+=a*t
    print(f'Data Set {T+1}:\n%.2f'%h)