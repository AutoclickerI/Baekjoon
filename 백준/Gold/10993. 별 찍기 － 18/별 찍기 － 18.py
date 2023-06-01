p=int(input())+1
a=['*']
for n in range(2,p):
    if n%2!=0:
        a=list(reversed(a))
    b=['*'*(2**(n+1)-3)]
    for j in range(1, 2**n-2):
        if j<=len(a):
            b.append(' '*j+'*'+' '*(2**(n-1)-1-j)+a[j-1]+' '*(2**(n-1)-1-j)+'*'+' '*j)
        else:
            b.append(' '*j+'*'+' '*(2**(n+1)-5-2*j)+'*'+' '*j)
    b.append(' '*(2**n-2)+'*'+' '*(2**n-2))
    a=b
    if n%2!=0:
        a=list(reversed(b))
for j in a:
    n=len(j)
    while j[n-1]==' ':
        n-=1
    print(j[:n])