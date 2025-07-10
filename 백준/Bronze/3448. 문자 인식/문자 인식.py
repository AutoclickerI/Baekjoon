s=[]
for*i,_ in[*open(0)][1:]:
 s+=i;x=round(100*(1-s.count('#')/len(s)),1)
 if[]==i:print(f'Efficiency ratio is {[int(x),x][0<x%1]}%.');s=[]