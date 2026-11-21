d={}
for i in[0]*int(input()):
    p,q=input().split()
    d[p]=int(q)
print(d['jinju'])
print(sum(d[i]>d['jinju'] for i in d))