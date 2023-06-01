N=int(input())
a,b,c,d,e,f=map(int,input().split())
if N==1:print(a+b+c+d+e+f-max(a,b,c,d,e,f))
else:print((5*N-6)*(N-2)*min(a,b,c,d,e,f)+(8*N-12)*min(a+b,a+c,a+d,a+e,b+c,b+d,b+f,c+e,c+f,d+e,d+f,e+f)+4*min(a+b+c,a+b+d,a+d+e,a+e+c,f+b+c,f+b+d,f+d+e,f+e+c))