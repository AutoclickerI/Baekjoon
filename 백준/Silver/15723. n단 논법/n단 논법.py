d=[26*[0]for _ in[0]*26]

for _ in[0]*int(input()):
    a,_,b=input().split()
    d[ord(a)-97][ord(b)-97]=1

for m in range(26):
    for s in range(26):
        for e in range(26):
            d[s][e]|=d[s][m]*d[m][e]

for _ in[0]*int(input()):
    a,_,b=input().split()
    print('FT'[d[ord(a)-97][ord(b)-97]])