ans, prv = 0, -1

for x in map(int,[*open(0)][1].split()):

    if prv + 1 == x:

        ans = -1

        break

    ans += x - prv + 1 >> 1    

    prv = x

print(ans)