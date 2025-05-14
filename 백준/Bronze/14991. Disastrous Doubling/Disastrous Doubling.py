for i in[*open(0)][b:=1].split():b=2*b-int(i)
print([b%(10**9+7),'error'][b<0])