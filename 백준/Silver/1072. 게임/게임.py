x,y=map(int,input().split())
z=y*100//x
print(1+~(z>98)or(x-100*y+z*x-1)//(99-z)+1)