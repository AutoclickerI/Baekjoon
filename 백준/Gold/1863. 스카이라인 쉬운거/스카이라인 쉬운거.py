s=[]
for i in*open(c:=0).read().split()[2::2],0:
 while[i:=int(i)]<=s[-1:]:c+=i<s.pop()
 s+=i,
print(c)