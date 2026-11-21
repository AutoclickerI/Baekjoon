a=b=c=0
for i in[*open(0)][1:]:
    t,s=i.split()
    if'i'==t[4]:a,b,c=a+1,0,0;print(a,s)
    elif'u'>t[4]:b,c=b+1,0;print(f'{a}.{b}',s)
    else:c+=1;print(f'{a}.{b}.{c}',s)