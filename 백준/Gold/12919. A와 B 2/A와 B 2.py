l=[input()]
T=input()

chk=T+' '+T[::-1]

for i in l:
    if i==T:
        exit(print(1))
    if i+'A'in chk:
        l+=i+'A',
    if'B'+i[::-1]in chk:
        l+='B'+i[::-1],
print(0)
