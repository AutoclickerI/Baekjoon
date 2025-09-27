*s,='0123'
exec("s+=str(eval('+'.join(s[-4:]))),;"*33)
for i in[*open(0)][1:]:l=i.split();print('NAUTILUS'*(s[:len(l)]==l)or'SNAIL')