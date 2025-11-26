R=60
def f():x,y,z=map(int,input().split(':'));return(x*R+y)*R+z
t=(~f()+f())%86400+1
print((3*'%02d:'%(t/R/R,t/R%R,t%R))[:8])