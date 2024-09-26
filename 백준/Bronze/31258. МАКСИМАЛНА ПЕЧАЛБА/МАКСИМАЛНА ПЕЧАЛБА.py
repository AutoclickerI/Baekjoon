f=lambda n:sorted(map(int,input().split()))[-n:]
print(c:=min(f(0)),sum(map(int.__mul__,f(c),f(c))))