f='ouehr'.find
t,*l=open(0)
t=int(t[:-3])
for i in l:a,b,c,d=i.split();t-=(f(c[1])-f(a[1]))*24+int(d)-int(b)
print(-(48<t)or(0<t)*t)