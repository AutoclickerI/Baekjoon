l=[*open(0)][1].split()

f=0

m=0
for i in l:
    if i=='1':
        m-=1
    else:
        m+=1
    if m<=0:
        m=0
        f=1

m=0
for i in l[::-1]:
    if i=='1':
        m-=1
    else:
        m+=1
    if m<=0:
        m=0
        f=1
        
cnt=l.count('1')

if cnt*2>=len(l):
    print(0)
elif f and cnt*2>=len(l)-m:
    print(1)
else:
    print(2)