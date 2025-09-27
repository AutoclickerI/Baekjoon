def trans(y,m,d):
    return 365*y+y//4-y//100+y//400+sum([0,31,28,31,30,31,30,31,31,30,31,30,31][:m])+d-(y%4<1 and(0<y%100 or y%400<1))*((m,d)<=(2,29))

y,m,d=map(int,input().split())
Y,M,D=map(int,input().split())
t=trans(Y,M,D)-trans(y,m,d)
if(y+1000,m,d)<=(Y,M,D):print('gg')
else:print(f'D-{t}')