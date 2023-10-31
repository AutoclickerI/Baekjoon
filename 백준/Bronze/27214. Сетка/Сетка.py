k,w,h,t=map(int,open(0))
l=['*'*(k*w+(w+1)*t)]*t
s=[(t*'*').join(['']+['.'*k]*w+[''])]*k
print(*(l+s)*h+l)