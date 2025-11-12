r,c,x,y=map(int,[*open(0)][1].split())
a=abs(r-x)
b=abs(c-y)+a//2
print((a|b)%-2or max(a,b)//2)