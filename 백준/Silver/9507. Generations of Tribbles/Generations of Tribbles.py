l=[1]
exec('l+=sum(l[-4:]),;'*99)
for i in[*open(0)][1:]:print(l[int(i)])