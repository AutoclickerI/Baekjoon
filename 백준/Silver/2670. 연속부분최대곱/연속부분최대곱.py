v=1
print('%.3f'%max(v:=max(x:=eval(i),v*x)for i in[*open(0)][1:]))