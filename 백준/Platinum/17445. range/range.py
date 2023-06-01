s=input()
l=eval(s)
li=[*map(int,s[6:-1].split(','))]
if l:
    if len(l)-1:
        if len(li)==3:a,b,c=li
        elif len(li)==2:a,b=li;c=1
        else:b=li[0];a,c=0,1
        hh=2*(c>0)-1
        if hh>0:p,q=a+(b-a-1)//c*c+1,a+(b-a-1)//c*c+c
        else:p,q=a+(b-a+1)//c*c+c,a+(b-a+1)//c*c-1
        if p<=-1<=q:an=-1
        elif len(str(p))==len(str(q)):an=p if abs(p)<abs(q)else q
        else:an=-int('1'+'0'*len(str(abs(q)))) if abs(p)>abs(q)else int('1'+'0'*(len(str(abs(q)))-1))
        if c-1:answ=f'range({a},{an},{c})'
        else:answ=f'range({a},{an})'
    else:
        c=l[-1]
        answ='range(1)'if c==0else'range(-1,-10,-10)'if c==-1else'range(-2,-1)'if c==-2else 0
        if answ==0:
            t=li[0]
            h=20*(c<0)-10
            while len(range(t,-1,h))-1:h*=10
            answ=f'range({t},-1,{h})'
else:answ='range(-1)'
print(answ)