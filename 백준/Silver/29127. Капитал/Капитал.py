a,n=map(int,input().split())
z=''
exec('z+=str(t:=min(a,9));a-=t;'*n)
print(-(0<a)or z)