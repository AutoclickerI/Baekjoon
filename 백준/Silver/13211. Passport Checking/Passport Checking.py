n,*l=open(0)
s={*l[:int(n)]}
print(sum(i in s for i in l[int(n):]))