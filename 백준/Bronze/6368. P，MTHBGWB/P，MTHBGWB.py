s=[bin(ord(i)-63)[3:]for i in'EVTJB\H^FWIZCDGXQLNAM]KUSR']
k={'_':'1100','.':'0001',',':'1010','?':'0'*4}
o={k[i]:i for i in k}
for i in range(int(input())):
    v,w,z='',[],''
    for t in input():
        if t in k:v+=k[t];w+=4,
        else:x=ord(t)-65;v+=s[x];w+=[len(s[x])]
    for j in w[::-1]:t,v=v[:j],v[j:];z+=o.get(t)or chr(s.index(t)+65)
    print(f'{i+1}:',z)