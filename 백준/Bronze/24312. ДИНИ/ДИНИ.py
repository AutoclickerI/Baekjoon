p,q,r,s=map(int,input().split())
a=p+q+r+s
print(min(map(abs,[a-2*p,a-2*q,a-2*r,a-2*s,a-2*(p+q),a-2*(r+q),a-2*(p+r)])))