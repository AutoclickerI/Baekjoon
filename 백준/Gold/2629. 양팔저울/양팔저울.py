s={0}
_,a,_,b=open(0)
for i in a.split():s|={j+int(i)for j in s}|{j-int(i)for j in s}
for i in b.split():print('NY'[int(i)in s])