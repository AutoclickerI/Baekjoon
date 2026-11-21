a,b=1,100
exec('a,b=max(len(input()),min(a,b)),a;'*int(input()))
print(min(a,b))