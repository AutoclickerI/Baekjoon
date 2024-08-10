n,a=open(0)
print(sum(ord(i)-96for i in a[:-1])*(len(a)<int(n)+2)or'Impossible')