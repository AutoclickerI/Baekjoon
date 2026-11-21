*A,X=open(i:=0)
for x in X.split():i+=1;A[:~int(x)]+=i,
print(*A[:i])