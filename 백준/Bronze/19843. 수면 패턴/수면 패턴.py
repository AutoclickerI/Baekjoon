f='ouehr'.find
t,*l=map(str.split,open(0))
t=int(t[0])
for a,b,c,d in l:t-=(f(c[1])-f(a[1]))*24+int(d)-int(b)
print(-(48<t)or max(t,0))