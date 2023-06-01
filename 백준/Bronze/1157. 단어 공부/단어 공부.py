from collections import Counter
a = list(input().upper())
a = Counter(a).most_common()
try:
    if a[0][1] == a[1][1]:
        print('?')
    else:
        print(a[0][0])
except:
    print(a[0][0])