f=''.join
for i in[*open(0)][1:]:l=[f'{int(x):06b}'for x in i.split(':')];print(f(map(f,zip(*l))),f(l))