s=input()
a=0
def check(r):
    if r=='0':
        return 1
    if r[0]=='0':
        return 0
    return int(r)<256
for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                if i+j+k+l+4==len(s):
                    a+=all(map(check,[s[:i+1],s[i+1:i+j+2],s[i+j+2:i+j+k+3],s[i+j+k+3:]]))
print(a)