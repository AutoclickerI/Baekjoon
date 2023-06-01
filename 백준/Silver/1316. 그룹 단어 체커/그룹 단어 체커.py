c = 0
for i in range(int(input())):
    a = []
    b = input()
    j = 0
    Flag = False
    while j < len(b):
        if b[j] not in a:
            a.append(b[j])
            if j + 1 == len(b):
                pass
            else:
                try:
                    while b[j] == b[j + 1]:
                        j += 1
                except:
                    pass
            j += 1
        else:
            Flag = True
            j += 1
    if Flag == False:
        c += 1
print(c)