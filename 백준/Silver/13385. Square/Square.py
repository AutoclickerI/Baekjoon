for i in[*open(0)][1:]:
 _,*a,l=map(int,i.split());w=1
 for n in a[::-1]:w,l=l,w+l*n
 print(l)