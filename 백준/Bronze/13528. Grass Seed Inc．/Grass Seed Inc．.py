a,b,*c=map(eval,open(0).read().split())
print(a*sum(c[2*i]*c[2*i+1]for i in range(b)))