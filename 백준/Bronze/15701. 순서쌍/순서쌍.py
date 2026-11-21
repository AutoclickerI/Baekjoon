n=int(input())
a,i=0,1
while i*i<n:a+=n%i<1;i+=1
print(2*a+(i*i==n))