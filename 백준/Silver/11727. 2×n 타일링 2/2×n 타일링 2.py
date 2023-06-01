l=[1,3]
exec('l+=[l[-2]*2+l[-1]];'*int(input()))
print(l[-3]%10007)