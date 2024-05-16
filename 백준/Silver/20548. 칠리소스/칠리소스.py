c=int(input())
a,i=0,1
while c:a+=c%7*i;i*=3;c//=7
print(a)