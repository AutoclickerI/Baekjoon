for i in[*open(0)][1:]:
 x,y=map(int,i.split());i=j=1
 while y>=i<i+j<=x:i,j=i+j,i
 print(i,j)