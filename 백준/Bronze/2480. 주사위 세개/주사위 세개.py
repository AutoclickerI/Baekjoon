a = input().split(' ')
a.sort()
if a[0] == a[1]:
    if a[1] == a[2]:
        print(10000 + int(a[0])*1000)
    else:
        print(1000 + int(a[0])*100)
else:
    if a[1] == a[2]:
        print(1000 + int(a[1])*100)
    else:
        print(int(a[2])*100)