a,[p,q,*b]=[[int(j,16)for j in i[:-1]]for i in open(0)]
k,K=p^2,q
S='%X%X'
s=S%(k,K)
for i in range(0,len(a),2):k^=a[i]^b[i];K^=a[i+1]^b[i+1];s+=S%(k,K)
print(s)