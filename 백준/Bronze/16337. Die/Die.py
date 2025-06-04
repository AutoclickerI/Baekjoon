s=[16,257,68,84,273,325,341,455,365]
f=str.replace
l=f(f(input()+input()+input(),*'o1'),*':0')
print(['unknown',l.count('1')][int(l,2)in s])