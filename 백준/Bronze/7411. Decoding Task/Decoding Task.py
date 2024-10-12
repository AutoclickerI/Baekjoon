a,b=[[int(j,16)for j in i[:-1]]for i in open(0)]
k,K=b[0]^2,b[1]
S='%X%X'
s=S%(k,K)
for i in range(0,len(a),2):k^=a[i]^b[i+2];K^=a[i+1]^b[i+3];s+=S%(k,K)
print(s)