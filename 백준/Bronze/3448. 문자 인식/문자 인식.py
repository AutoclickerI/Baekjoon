s=''
for i in[*open(0)][1:]:
 s+=i[:-1]
 if' '>i:x=round(100*(1-s.count('#')/len(s)),1);print(f'Efficiency ratio is {[int(x),x][0<x%1]}%.');s=''