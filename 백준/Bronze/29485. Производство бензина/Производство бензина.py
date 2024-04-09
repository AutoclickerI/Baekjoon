n,*a=[[*map(int,i.split())]for i in open(0)]
print(min(range(*n),key=lambda i:a[i][0]/(a[i][2]-a[i][1]))+1)