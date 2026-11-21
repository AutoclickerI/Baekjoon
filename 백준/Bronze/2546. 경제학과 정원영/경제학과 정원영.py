_,*l=[[*map(int,i.split())]for i in open(0)]
for(n,m),i,j in zip(l[1::4],l[2::4],l[3::4]):s,t=sum(i),sum(j);print(sum(t/m<c<s/n for c in i))