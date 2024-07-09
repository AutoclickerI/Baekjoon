def RATS(s):
    return ''.join(sorted(str(int(s)+int(s[::-1])))).strip('0')
for _ in[0]*int(input()):
    K,M,d=input().split()
    s=set()
    for i in range(1,int(M)+1):
        if d in s:
            print(K,'R',i)
            break
        if d[:3]=='123'and d[-4:]=='4444'and{*d[3:-4]}=={'3'}or d[:3]=='556'and d[-4:]=='7777'and{*d[3:-4]}=={'6'}:
            print(K,'C',i)
            break
        s.add(d)
        prevd=d
        d=RATS(d)
    else:
        print(K,prevd)