s=input()
S={s}
for _ in[0]*int(input()):
    p,q=input().split()
    if s==q:s=p;S.add(s)
print(s,len(S))