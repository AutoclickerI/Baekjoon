n,s=open(0)
print('TNAIKE'[all({*'012'}-{*s[i:i+6]}for i in range(2*int(n)))::2])