l=[float(input())for i in range(int(input())+1)]
def f(x,a=0,b=0,c=0,d=0,e=0,f=0,g=0,h=0,i=0,j=0,k=0,l=0):
    return a+b*x+c*x**2+d*x**3+e*x**4+f*x**5+g*x**6+h*x**7+i*x**8+j*x**9+k*x**10+l*x**11
ans=[-1000000,1000000]
for i in range(100):
    p=sum(ans)/len(ans)
    if f(p,*l)*f(ans[0],*l)>0:
        ans[0]=p
    else:
        ans[1]=p
print(int(ans[0]*1000))