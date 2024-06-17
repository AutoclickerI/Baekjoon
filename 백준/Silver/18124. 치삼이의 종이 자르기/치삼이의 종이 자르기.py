N=int(input())
l=1
a=0
while N>2*l:a+=l;l<<=1
print(a+(N>l)*-~N//2)