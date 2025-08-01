r=lambda:range(int(input()))
g=lambda:map(int,input().split())
for _ in r():
    r();s,l={*g()},[]
    for N in r():
        x,y,z=g()
        if(x in s)*(0<=y<6or(y==6 and z==0)):l+=[[y*60+z,x]]
    print(min(l)[1],len(l))