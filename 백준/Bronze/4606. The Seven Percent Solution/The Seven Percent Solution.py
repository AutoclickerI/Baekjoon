s=open(0).read()[:-2]
for i in'% !$()*':s=s.replace(i,f'%{ord(i):x}')
print(s)