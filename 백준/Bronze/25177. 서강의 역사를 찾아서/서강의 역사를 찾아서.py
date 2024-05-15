f=lambda:[*map(int,input().split())]
f()
print(max(0,*(y-x for x,y in zip(f()+[0]*999,f()))))