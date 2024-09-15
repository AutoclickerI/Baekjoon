a,b=open(0)
print(*['Bad luck']if len(b)>len(a)*(a!=b)else[0]*(int(a)>int(b))or[1,[i+1for i in range(len(a))if a[i]<b[i]][0]])