s=sorted
t,n=zip(*s((int(input()),i)for i in range(1,9))[3:])
print(sum(t),*s(n))