a,b=open(i:=0)
for j in range(len(b)-1):i+=b[j]==a[i%~-len(a)]
print(i//~-len(a))