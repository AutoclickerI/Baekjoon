from itertools import*
s,e=input().split()
c=0
while s!=e:c+=1;s=''.join(f'{len([*g])}{i}'for i,g in groupby(s))
print(c)