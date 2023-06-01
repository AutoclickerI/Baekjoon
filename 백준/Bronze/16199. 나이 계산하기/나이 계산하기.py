a,b,c=map(int,input().split())
d,e,f=map(int,input().split())
man=d-a
man=man-1 if (e<b or (e==b and f<c)) else man
print(man,d-a+1,d-a,sep='\n')