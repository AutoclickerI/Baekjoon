a,b=open(i:=0)
for j in range(len(b)):i+=b[j]==a[i%~-len(a)]
print(i//~-len(a))