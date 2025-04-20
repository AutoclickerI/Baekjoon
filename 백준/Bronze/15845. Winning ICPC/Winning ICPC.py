(n,m),t,*l=[[*map(int,i.split())]for i in open(0)]
v=[sum(i==j for i,j in zip(k,t))for k in l]
print(max(range(n),key=lambda i:v[i])+1)