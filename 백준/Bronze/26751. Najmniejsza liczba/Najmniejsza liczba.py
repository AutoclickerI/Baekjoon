*_,p,q,r=sorted(input())
print(min(z for z in[p+q+r,q+p+r,r+p+q]if'0'<z[0]))