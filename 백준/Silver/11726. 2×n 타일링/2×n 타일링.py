l=[1,2]
exec('l+=[l[-2]+l[-1]];'*int(input()))
print(l[-3]%10007)