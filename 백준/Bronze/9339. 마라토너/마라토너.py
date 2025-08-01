_,*l=[[*map(int,i.split())]for i in open(0)]
while l:_,s,[n],*l=l;print(min(z:=[(y*60+z,x)for x,y,z in l[:n]if(x in s)*(0<=y<6or(z<1<6==y))])[1],len(z));l=l[n:]