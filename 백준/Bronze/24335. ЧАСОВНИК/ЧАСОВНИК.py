h,m,dh,dm,c=map(int,input().split())
h+=dh
m+=dm
h+=m//60
m%=60
h%=12
if c==1:
    print(h,m)
else:
    if m%12:
        print((h*5+m//12)%60,(h*5+m//12+1)%60)
    else:
        print('@',(h*5+m//12)%60)