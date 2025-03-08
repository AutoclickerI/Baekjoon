h,*l=map(int,[*open(a:=0)][1].split())
for i in l:a+=h;h=min(h,i)
print(a)