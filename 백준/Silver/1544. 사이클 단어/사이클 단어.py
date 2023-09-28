s=set()
for _ in[0]*int(input()):
    n=len(S:=input())
    t=S*2
    s.add(min(t[i:i+n]for i in range(n)))
print(len(s))