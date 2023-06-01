a,x,b,y,T=[int(input())for i in[0]*5]
if T<31:print(a,b)
elif T<46:print((T-30)*x*21+a,b)
else:print((T-30)*x*21+a,(T-45)*y*21+b)