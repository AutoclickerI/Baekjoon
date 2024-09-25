a,b,c,d,e,f=map(int,input().split())
g,h,i,j,k,l=map(int,input().split())
f=lambda a,b,g,h:g<=a<h or g<b<=h or a<=g<b or a<h<=b
print(f(a,b,g,h)*f(c,d,i,j)-1or e-l+1)