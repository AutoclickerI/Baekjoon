n,*l=open(0)
t=sum(int(s[0])*60+int(s[2:])for s in l)-int(n[-3:])*~-len(l)
print(f'{t//3600:02d}:{t%3600//60:02d}:{t%60:02d}')