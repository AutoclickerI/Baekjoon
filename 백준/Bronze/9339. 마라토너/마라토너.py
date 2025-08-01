_,*l=[map(int,i.split())for i in open(0)]
while l:_,s,[n],*l=l;s={*s};z=[(y*60+z,x)for x,y,z in l[:n]if(x in s)*(0<=y<6or(z<1<6==y))];print(min(z)[1],len(z));l=l[n:]