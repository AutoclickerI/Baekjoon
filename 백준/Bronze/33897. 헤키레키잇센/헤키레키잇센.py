m=s=p=0
c=1
for i in[*open(0)][1].split():f=p>(p:=int(i));c+=f;m=max(s:=+f or-~s,m)
print(c,m)