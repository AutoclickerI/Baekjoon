_,*l=open(0)
print(min(l,key=lambda x:(-l.count(x),x)))