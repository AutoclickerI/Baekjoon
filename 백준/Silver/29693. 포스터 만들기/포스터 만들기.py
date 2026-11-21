l,s,*X=open(0)
n,m=map(int,l.split())
a=m-3>>1
for i in range(1,n):{*X[i-1][a:a+4-m%2]}=={'X'}<exit(print('YES\n'+s*i+'B'*a+'WY'+~m%2*'Y'+'W'+'B'*a+'\n'+s*(n+~i)))
print('NO')