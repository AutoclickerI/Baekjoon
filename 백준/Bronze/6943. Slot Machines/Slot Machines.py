n,*c=map(int,open(0))
l=[(35,30),(100,60),(10,9)]
a=i=0
while n:
    c[i]+=1
    if c[i]==l[i][0]:c[i]=0;n+=l[i][1]    
    a+=1;i=(i+1)%3;n-=1
print('Martha plays',a,'times before going broke.')