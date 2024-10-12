n=int(input())

a=eval("input().replace(' ',''),"*n)
b=eval("input().replace(' ',''),"*n)

def flip(l):
    return tuple(i[::-1]for i in l)
def rotate(l):
    return tuple(''.join(i).strip()[::-1]for i in zip(*[i.rjust(n)for i in l]))
def diff(*l):
    return sum(i!=j for k in zip(*l)for i,j in zip(*k))
print(min(map(diff,[b]*6,[a,flip(a),rotate(a),flip(rotate(a)),rotate(rotate(a)),flip(rotate(rotate(a)))])))