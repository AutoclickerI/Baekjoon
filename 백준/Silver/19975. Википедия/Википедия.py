import re
r=lambda:range(int(input()))
f=lambda s:s[0].lower()+s[1:]
l=[]
d={}
for T in r():
    k=input();d[f(k)]=k
    for i in r():d[f(input())]=k
    l+=(k,[input()for i in r()]),
for k,w in l:
    print(k)
    for s in w:
        a=[]
        for i in re.findall('[A-Za-z]+|.',s):
            j=f(i)
            if j in d and(b:=d[j])!=k:
                if j==f(b):a+=f'[[{i}]]'
                else:a+=f'[[{b}|{i}]]'
            else:a+=i
        print(''.join(a))