N=int(input())
b=[[*input()]for _ in[0]*N]
f=all(N==len({*i})for i in b)
z=b[0]!=sorted(b[0])
b=[[*i]for i in zip(*b)]
f&=all(N==len({*i})for i in b)
z|=b[0]!=sorted(b[0])
if f:
    print('Not '*z+'Reduced')
else:
    print('No')