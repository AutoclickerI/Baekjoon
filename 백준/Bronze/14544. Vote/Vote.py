r=range
for T in r(int(input())):
    n,q=map(int,input(f'VOTE {T+1}: ').split());d={input():0 for i in r(n)}
    for i in r(q):x,y,z=input().split();d[x]+=int(y)
    d=sorted([[d[i],i] for i in d])
    if len(d)==1 or(a:=d[-1])[0]>d[-2][0]:print('THE WINNER IS',*a[::-1])
    else:print('THERE IS A DILEMMA')