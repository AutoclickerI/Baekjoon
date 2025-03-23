s={1:1}

for _ in[0]*~-int(input()):
    t={}
    for i in s:
        t[i*2]=t.get(i*2,0)+s[i]
        if i%3==1 and i//3%2 and 1<i//3:
            t[i//3]=t.get(i//3,0)+s[i]
    s=t
    

print(sum(s.values()))
for i in sorted(s):
    print(i)