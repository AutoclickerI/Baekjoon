a=[1,1,1,1,2,2,3,4,5]
for i in range(93):a.append(a[-1]+a[i+4])
[print(a[int(input())])for i in range(int(input()))]