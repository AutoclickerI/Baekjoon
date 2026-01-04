_,*l=open(0)
while l:_,i,j,*l=l;print(max(map([*zip(i,j)].count,[(*'WB',),(*'BW',)])))