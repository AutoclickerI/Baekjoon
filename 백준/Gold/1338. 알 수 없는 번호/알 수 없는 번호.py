s,e,x,y=map(int,open(0).read().split())
s,e=sorted([s,e])
x=abs(x)
k=(e-y)//x
v=k*x+y
if x<=y or y<0 or (not s<=v)or s<=v-x:
    print('Unknwon Number')
else:
    print(v)