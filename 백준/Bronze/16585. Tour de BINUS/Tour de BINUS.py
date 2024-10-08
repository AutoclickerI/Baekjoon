_,r,(x,d),(X,D)=map(str.split,open(0))
*r,x,X=map(int,r+[x,X])
print(sum(r[x-1::2*('m'<d)-1]),r[X-1::2*('m'<D)-1].count(0))