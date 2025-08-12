a,b=input().split()
m,n=len(a),len(b)
i=c=0
while{z:=a[c]}-{*b}:c+=1
while i<n:print(['.'*c+b[i]+'.'*m,a][i==b.find(z)][:m]);i+=1