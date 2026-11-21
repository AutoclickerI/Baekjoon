a=b=c=1
exec('a,b,c=b,c,a+c;'*~-int(input()))
print(a)