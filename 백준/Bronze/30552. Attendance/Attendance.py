l=*[*open(0)][1:],''
t=1
f=1
for i in l:
    if'Present!\n'==i:
        f=1
    else:
        t&=f
        f or print(end=p)
        f=0
    p=i
if t:
    print('No Absences')