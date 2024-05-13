*a,b=open(0).read().split()
print(sum(i>b==i[:len(b)]for i in a))