n,l=open(0)
print(sorted(l.split(),key=int)[~int(n)//2])