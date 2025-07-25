s=p=0
print(max(s:=s-s*(p==i=='0')+('0'<(p:=i))for i in[*open(0)][1].split()))