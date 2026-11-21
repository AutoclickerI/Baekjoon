(h,w,q),*l=[map(int,i.split())for i in open(0)]
a=w*h*[0]
m=a[:]
for o,x,y,*c in l:
 for i in 0,1,2,3:m[t:=(x-i//2)*w+y-i%2]|=o>1;a[t]=[*c,a[t]][-m[t]]
print(*a)