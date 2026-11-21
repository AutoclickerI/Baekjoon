r=0
print(sum(r:=min(r+1,int(i))for i in[*open(0)][1].split()[::-1]))