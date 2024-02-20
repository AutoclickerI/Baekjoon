for _ in[0]*int(input()):
    p,q=input().split()
    bit=''
    for i in q:
        bit+=('000'+bin(int(i,16))[2:])[-4:]
    if bit=='0'*32:
        print(p,'0'*8)
        continue
    newbit=bit[0]
    exp=4*int(bit[1:8],2)-257
    mantissa=bit[8:]
    while exp<-126:
        exp+=1
        mantissa='0'+mantissa[:-1]
    while -126<exp and mantissa[0]=='0':
        exp-=1
        mantissa=mantissa[1:]+'0'
    if exp>127:
        newbit+='1'*8+'0'*23
    else:
        if mantissa[0]=='0':
            newbit+='0'*8+mantissa[1:]
        else:
            newbit+=('00000000'+bin(exp+127)[2:])[-8:]+mantissa[1:]
    print(p,''.join('%X'%int(newbit[4*i:4*i+4],2)for i in range(8)))