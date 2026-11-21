r=q=w=0
for i in[*open(0)][1:]:a,b=i.split();r+=(b==a!='0')+(q==a!='0')+(w==b!='0');q,w=a,b     
print(r)