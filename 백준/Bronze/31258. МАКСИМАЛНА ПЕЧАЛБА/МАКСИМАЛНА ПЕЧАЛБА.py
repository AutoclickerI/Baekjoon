f=lambda:sorted(map(int,input().split()))[::-1]
print(c:=min(f()),sum(map(int.__mul__,f(),f())))