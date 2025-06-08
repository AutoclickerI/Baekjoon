def f(s):
    i=0
    while i*i<len(s):i+=1
    s+='*'*(i*i-len(s))
    return''.join(''.join(i[::-1])for i in zip(*zip(*[iter(s)]*i))).replace('*','')
for _ in[0]*int(input()):
    print(f(input()))