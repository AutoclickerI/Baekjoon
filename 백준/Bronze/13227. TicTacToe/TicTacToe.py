s=open(0).read()
print('NYOE S'[any(s[m-i:m-~i:i]in'OOO XXX'for m,i in zip(b'	',b''))::2])