m,n=map(int,input().split())
q=''
while m:q=f'{m%n:X}'+q;m//=n
print(q or 0)