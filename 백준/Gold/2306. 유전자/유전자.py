from functools import*

s=input()
@cache
def f(i,j):
    if j<i+2:
        return 0
    if i+2==j:
        return s[i:i+2]in('at','gc')
    return max((s[i]+s[j-1]in('at','gc'))+f(i+1,j-1),f(i+1,j),f(i,j-1),max(f(i,k)+f(k,j)for k in range(i+1,j-1)))

print(f(0,len(s))*2)