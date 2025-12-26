m=1e9
print(max(int(i)-(m:=min(m,int(i)))for i in[*open(0)][1].split()))