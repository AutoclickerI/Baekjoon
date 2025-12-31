*s,=input()
l=[]
v=[]
for i in range(len(s)):
    if s[i]=='(':
        v+=i,
    if s[i]==')':
        l+=(v.pop(),i),
r=[]
for i in range(1,2**len(l)):
    c=0
    t=s[:]
    while i:
        if i%2:
            p,q=l[c]
            t[p]=t[q]=''
        c+=1
        i//=2
    r+=''.join(t),
for i in sorted({*r}):
    print(i)