_,*l=open(0)
print(sum((i+i[::-1]).count('XY')for i in[*l,*map(''.join,zip(*l))]))