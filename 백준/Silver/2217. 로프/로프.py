a=[int(input())for i in range(int(input()))]
a.sort()
n=0
for i in range(len(a)):
    if a[0]*len(a)>n:
        n=a[0]*len(a)
    del a[0]
print(n)