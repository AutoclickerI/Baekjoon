n,s=open(0)
print('TNAIKE'[all({*'012'}-{*s[2*i:2*i+6]}for i in range(int(n)))::2])