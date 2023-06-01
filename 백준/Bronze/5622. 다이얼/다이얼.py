a = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
b = 0
c = input()
for i in range(len(c)):
    if a.index(c[i]) < 15:
        b += a.index(c[i])//3 + 3
    elif 15 <= a.index(c[i]) < 19:
        b += 8
    elif 19 <= a.index(c[i]) < 22:
        b += 9
    else:
        b += 10
print(b)