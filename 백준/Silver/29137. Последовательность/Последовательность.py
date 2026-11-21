a=0,0
for i in[*open(0)][1].split():a+=int(i)-sum(a[-2:]),
print(*a)