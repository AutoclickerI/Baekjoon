p=1e9
print(max((n:=int(i))-(p:=min(p,n))for i in[*open(0)][1].split()))