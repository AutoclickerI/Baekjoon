x=0
for i in[*open(0)][1:]:a,b=map(int,i.split());x-=~max(0,b-x%(a+b))
print(x)