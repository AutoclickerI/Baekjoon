s=['{}']
for i in range(15):s+='{'+','.join(s)+'}',
f=s.index
for _ in[0]*int(input()):print(s[f(input())+f(input())])