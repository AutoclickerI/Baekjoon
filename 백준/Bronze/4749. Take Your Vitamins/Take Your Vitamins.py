b=[]
while'.'<(s:=input()):
    A,U,R,*V=s.split();A,R=map(eval,[A,R]);a=A*100/R
    if a<1:b+=V,
    else:print(f"{' '.join(V)} {A:.1f} {U} {a:.0f}%")
print('Provides no significant amount of:')
for i in b:print(*i)