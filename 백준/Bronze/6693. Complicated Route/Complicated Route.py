E=1
N=1j
W=-1
S=-1j
SE=(S+E)/2**.5
NE=(N+E)/2**.5
NW=(N+W)/2**.5
SW=(S+W)/2**.5
while(s:=input().replace(*',+'))!='END':
    stack=[]
    for i,j in zip(s,s[1:]):
        stack+=i,
        if i.isdigit() and j.isalpha():
            stack+='*',
    v=eval(''.join(stack))
    print(f'You can go to ({v.real:.3f},{v.imag:.3f}), the distance is {abs(v):.3f} steps.')