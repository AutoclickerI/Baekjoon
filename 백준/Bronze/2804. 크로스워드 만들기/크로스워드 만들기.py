a,b=input().split()
m,n=len(a),len(b)
i=c=0
while(a[c]in b)<1:c+=1
while i<n:print(['.'*c+b[i]+'.'*(m+~c),a][i==b.find(a[c])]);i+=1