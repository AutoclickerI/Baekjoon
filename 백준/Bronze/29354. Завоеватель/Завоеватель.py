h=1e9
print(sum(h:=min(h,int(i))for i in[*open(0)][1].split()[:-1]))