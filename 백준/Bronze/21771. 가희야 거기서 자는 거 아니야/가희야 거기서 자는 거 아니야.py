l=(s:=open(0).read()).split()
print(+(eval(l[4]+'*'+l[5])>s.count('P')))