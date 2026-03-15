s=[0]

for i in input():
    if i=='(':
        s+='(',0
    elif i in'HCO':
        s+=[1,12,16]['HC'.find(i)],
    elif i.isdigit():
        s[-1]*=int(i)
    else:
        r=0
        while'('!=(c:=s.pop()):r+=c
        s+=r,
print(sum(s))