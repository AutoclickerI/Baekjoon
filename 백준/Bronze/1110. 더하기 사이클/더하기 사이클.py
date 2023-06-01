a = input()
if len(a) == 1:
    a = '0' + a
b = a
count = 0
while True:
    count += 1
    if len(a) == 1:
        a = '0' + a
    a = a[1] + str(int(a[0]) + int(a[1]))[-1]
    if a == b:
        break
print(count)
    