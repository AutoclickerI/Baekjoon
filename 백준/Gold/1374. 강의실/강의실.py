L=[]
for i in[*open(c:=0)][1:]:_,a,b=map(int,i.split());L+=(b,-1),(a,1)
print(max(c:=c+i for _,i in sorted(L)))