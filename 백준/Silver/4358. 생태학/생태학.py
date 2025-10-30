d={}
for i in open(c:=0):d[i]=d.get(i,0)+100;c+=1
for i in sorted(d):print(i+f'{d[i]/c:.4f}')