b=p=i=0
for c in[*open(0)][1]:i+=1;t=c=='O';p+=(i+b)*t;b=-~b*t
print(p)