b,r,f=map(input().find,'#@!')
print((f<b<r or r<b<f)*abs(r-f)-1)