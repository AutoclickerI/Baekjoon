t,*s='',
for u in[*open(0)][1:]:t+=str(v:=sum(i*'. 'in u for i in range(1,201)))+u[u.rfind(' '):];s+=v,
print(len({*s}),t)