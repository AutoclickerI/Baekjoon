for o in range(int(input())):
    print(f'PROGRAM #{o+1}:')
    try:
        printer=''
        l=[0]*32768
        pos=0
        s=''
        while 1:
            i,*_=input().split('%')
            if i=='end':break
            s+=i
        I=0
        cnt=0
        for i in s:
            if i=='[':cnt+=1
            if i==']':cnt-=1
            assert cnt>=0
        assert cnt==0
        while I<len(s):
            i=s[I]
            if i=='>':pos+=1
            elif i=='<':pos-=1
            elif i=='+':l[pos]+=1
            elif i=='-':l[pos]-=1
            elif i=='.':printer+=chr(l[pos])
            elif i=='[':
                if l[pos]==0:
                    cnt=1
                    I+=1
                    while s[I]!=']'or cnt!=1:
                        if s[I]==']':cnt-=1
                        if s[I]=='[':cnt+=1
                        I+=1
            elif i==']':
                if l[pos]!=0:
                    cnt=1
                    I-=1
                    while s[I]!='['or cnt!=1:
                        if s[I]==']':cnt+=1
                        if s[I]=='[':cnt-=1
                        I-=1
            I+=1
            l[pos]%=256;pos%=32768
    except:
        printer='COMPILE ERROR'
    print(printer)