f=lambda x:sum('..'in z for y in x for z in y.split('X'))
_,*s=open(0)
print(f(s),f(map(''.join,zip(*s))))