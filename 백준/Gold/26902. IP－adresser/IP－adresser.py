s=input()
a=0
R=range(1,4)
def check(r):
    if r=='0':
        return 1
    if r[0]=='0':
        return 0
    return int(r)<256
for i in R:
    for j in R:
        for k in R:
            for l in R:
                if i+j+k+l==len(s):
                    a+=all(map(check,[s[:i],s[i:i+j],s[i+j:i+j+k],s[i+j+k:]]))
print(a)