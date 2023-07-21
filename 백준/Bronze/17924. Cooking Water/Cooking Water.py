n=int(input())
p,q=map(int,input().split())
d={*range(p,q+1)}
for i in[0]*~-n:p,q=map(int,input().split());d&={*range(p,q+1)}
print('gunilla has a point'if d else'edward is right')