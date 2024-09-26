f=lambda n:sorted(map(int,input().split()))[-n:]
print(c:=min(f(0)),sum(a*b for a,b in zip(f(c),f(c))))