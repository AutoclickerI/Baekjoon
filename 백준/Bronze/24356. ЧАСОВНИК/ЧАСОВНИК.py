a,b,c,d=map(int,input().split())
t=((c-a)*60+d-b)%1440
print(t,t//30)