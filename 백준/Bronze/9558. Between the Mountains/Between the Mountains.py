f=lambda:[*map(int,input().split())][1:]
exec('a,b=f(),f();print(min(abs(x-y)for x in a for y in b));'*int(input()))