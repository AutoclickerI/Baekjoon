n = int(input())
i = 2
a={}
while n != 1:
    if n % i == 0:
        n = n // i
        try:
            a[i]+=1
        except:
            a[i]=1
    else:
        i += 1
for i in a.keys():
    n*=(i**(a[i]+1)-1)//(i-1)
print(n*5-24)