def get_ms(s):
    try:
        return int(s.split()[2][1:])
    except:
        exit()

l=1

print('Q'*l)
r=input()

while r=='ACCESS DENIED (5 ms)':
    l+=1
    print('Q'*l)
    r=input()

s='QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp1234567890'

db=['Q']*l

ms=get_ms(r)

for i in range(l):
    tmp=db[:]
    for j in s[1:]:
        tmp[i]=j
        print(*tmp,sep='')
        r2=input()
        ms2=get_ms(r2)
        if ms2<ms:
            break
        if ms==ms2:
            continue
        if ms<ms2:
            ms=ms2
            db=tmp
            break
print(*db)