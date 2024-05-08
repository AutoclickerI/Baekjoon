l=len(s:=input())
n=int(s)
print(l*(n//10+1)+(1-10**~-l)//9+(n>1)*(n%10>0)*l)