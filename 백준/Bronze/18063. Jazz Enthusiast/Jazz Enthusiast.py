n,*l=open(0)
m=int(n[-3:])
t=sum(int(s[0])*60+int(s[2:])for s in l)-m*~-len(l)
print(f'{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}')