f=1
exec('f&=s!=s[::-1];s=s[-1]+s[:-1];'*len(s:=input()))
print('yneos'[f::2])