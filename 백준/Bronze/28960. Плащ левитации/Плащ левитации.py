h,l,a,b=map(int,input().split())
print("YNEOS"[(h<a/2or l<b)*(h<b/2or l<a)::2])