a,b=open(0,'rb')
print(*sorted(map(abs,(a[0]-b[0],a[1]-b[1]))))