s=open(0).read()
a,b,c=s.split()
print('NYOE S'[any({*i}<{*'OX'}for i in(a,b,c,*zip(a,b,c),s[0::5],s[8::-3]))::2])