a,b,c,d,e,f,g,h,i,j,k,l=map(int,open(0).read().split())
p,q,r=((c-a)*60+d-b)%1440,((g-e)*60+h-f)%1440,((k-i)*60+l-j)%1440
print(f'{min(p,q,r)//60}:{min(p,q,r)%60:02d}')
print(f'{max(p,q,r)//60}:{max(p,q,r)%60:02d}')