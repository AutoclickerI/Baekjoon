s=input().replace(*'[ ')
a=0
a+=s.count(']')*8
s=s.replace(*'] ').split()
for i in s:
    if i.isdigit():a+=8
    else:a+=len(i)+12
print(a)