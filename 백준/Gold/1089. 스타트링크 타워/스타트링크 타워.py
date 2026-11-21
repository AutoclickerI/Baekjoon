n,*l=open(V:=0)
d={0:(7,5,5,5,7),1:(1,1,1,1,1),2:(7,1,7,4,7),3:(7,1,7,1,7),4:(5,5,7,1,1),5:(7,4,7,1,7),6:(7,4,7,5,7),7:(7,1,1,1,1),8:(7,5,7,5,7),9:(7,5,7,1,7)}
R=range
try:
    for i in[tuple(int(j.replace(*'.0').replace(*'#1')[4*i:4*i+3],2)for j in l)for i in R(int(n))]:assert any(C:=[all(i[k]|d[j][k]==d[j][k]for k in R(5))for j in R(10)]);V=10*V+sum(i*C[i]for i in R(10))/sum(C)
    print(V)
except:print(-1)