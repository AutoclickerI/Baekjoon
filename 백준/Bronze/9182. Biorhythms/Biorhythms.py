c=1
while'0'<(s:=input()):
    p,e,I,d=map(int,s.split())
    for i in range(1,1<<20):
        if max((d+i-p)%23,(d+i-e)%28,(d+i-I)%33)<1:print(f'Case {c}: the next triple peak occurs in {i} days.');c+=1;break