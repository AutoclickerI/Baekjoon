a = input().split(' ')
h = int(a[0])
m = int(a[1]) - 45
if m < 0:
    m += 60
    h -= 1
if h < 0:
    h += 24
print(f'{h} {m}')
