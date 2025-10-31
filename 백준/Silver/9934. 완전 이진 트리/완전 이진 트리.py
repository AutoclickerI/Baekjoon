l=[[*open(0)][1].split()]
for i in l:
 if i:print(i[v:=len(i)//2]);l+=i[:v],i[v+1:]