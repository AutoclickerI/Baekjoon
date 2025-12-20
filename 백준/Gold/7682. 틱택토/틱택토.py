d={}
v=['.']*9
def check():
    if{'O'}in({*v[:3]},{*v[3:6]},{*v[6:9]},{*v[::3]},{*v[1::3]},{*v[2::3]},{*v[::4]},{*v[2:-1:2]}):
        return 0
    if{'X'}in({*v[:3]},{*v[3:6]},{*v[6:9]},{*v[::3]},{*v[1::3]},{*v[2::3]},{*v[::4]},{*v[2:-1:2]}):
        return 0
    if'.'not in v:
        return 0
    return 1
    
def backtrack(n):
    for i in range(9):
        if v[i]=='.':
            v[i]='XO'[n%2]
            if check():
                backtrack(n+1)
            else:    
                d[''.join(v)]=0
            v[i]='.'
backtrack(0)

for i in[*open(0)][:-1]:
    print(d.get(i[:-1],1)*'in'+'valid')