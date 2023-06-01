a,b,c,d,e=input().split()
def ev(p,q,r):
    if q=='+':
        return p+r
    if q=='-':
        return p-r
    if q=='/':
        return abs(p)//abs(r)*((p*r>0)*2-1)
    if q=='*':
        return p*r
l=[ev(ev(int(a),b,int(c)),d,int(e)),ev(int(a),b,ev(int(c),d,int(e)))]
print(min(l),max(l))