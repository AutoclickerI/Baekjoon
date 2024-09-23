_,[*a],_,b=eval('map(int,input().split()),'*4)
for q in b:q-=1;a[q]+=a[q]<2019&~-(a[q]+1in a)
print(*a)