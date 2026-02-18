from math import*
for i in[*open(0)][1:]:x,y,a,b=map(int,i.split());print(2*asinh(hypot(a-x,b-y)/2/sqrt(y*b)))