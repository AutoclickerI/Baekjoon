s,*t=[*map(int,open(i:=0))],
for j in s:T=[];exec('T+=j,;j=s[j];'*99);t+=[i]*(i in T);i+=1
print(len(t),*t)