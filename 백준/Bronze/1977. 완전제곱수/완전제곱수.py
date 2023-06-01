a=[]
for i in range(int(input()),int(input())+1):
    if i**0.5==int(i**0.5):
        a.append(i)
try:
    n=a[0]
    print(sum(a));a.sort();print(a[0])
except:
    print(-1)