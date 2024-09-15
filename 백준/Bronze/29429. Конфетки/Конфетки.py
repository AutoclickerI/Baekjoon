a,b,*x=open(0)
if len(b)>len(a)or a==b:x+='Bad luck',
elif int(a)>int(b):x+=0,
else:x+=1,;x+=[i for i in range(len(a))if a[i]<b[i]][0]+1,
print(*x)