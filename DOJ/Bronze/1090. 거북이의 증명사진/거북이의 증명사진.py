s=0
for i in[*open(0)][1:]:
    h,f=map(int,i.split())
    s+=f<h
print(s)