s=0,1,2,3
exec('s=*s,sum(s[-4:]);'*33)
for i in[*open(0)][1:]:l=*map(int,i.split()),;print(['SNAIL','NAUTILUS'][s[:len(l)]==l])