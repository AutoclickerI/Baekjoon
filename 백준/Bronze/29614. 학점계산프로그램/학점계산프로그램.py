s=input()
a,b,c,d,p=map(s.count,'ABCD+')
print((4*a+3*b+2*c+d+p/2)/(len(s)-p))