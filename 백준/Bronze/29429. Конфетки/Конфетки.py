a,b=open(0)
print(*['Bad luck']if len(b)>len(a)or a==b else[0]*(int(a)>int(b))or[1,[i for i in range(len(a))if a[i]<b[i]][0]+1])