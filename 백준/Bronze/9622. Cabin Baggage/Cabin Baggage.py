a=0
for _ in[0]*int(input()):
    p,q,r,s=map(eval,input().split())
    print(s:=((p<=56)*(q<=45)*(r<=25)or(p+q+r<=125))*(s<=7))
    a+=s
print(a)