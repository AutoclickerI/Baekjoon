_,h,v=[[*map(int,i.split())]for i in open(0)]
t=0
while h<v:h=[i+1for i in h];t+=1
print(t)