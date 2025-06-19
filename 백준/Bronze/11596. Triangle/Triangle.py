f=lambda:sorted(map(int,input().split()))
a,b,c=d=f()
print('YNEOS'[d!=f()or a*a+b*b!=c*c::2])