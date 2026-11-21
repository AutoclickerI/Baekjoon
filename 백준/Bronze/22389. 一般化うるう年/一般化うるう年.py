R=range
while any(l:=[*map(int,input().split())]):n,l,r=l;a=[int(input())for i in R(n)];print(sum(~min([i for i in R(n)if j%a[i]<1]+[n])&1for j in R(l,r+1)))