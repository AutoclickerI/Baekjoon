n,*l=[[*map(int,i.split())]for i in open(0)]
def f(a):
 s=[1e9]
 for i in a[::-1]:
  while s[-1]<=i:s.pop()
  s+=i,
 return len(s)-1
print(*map(f,(*zip(*l),*l)))