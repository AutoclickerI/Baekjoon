for T in[0]*int(input()):
    n=int(input())
    l=[int(input())for _ in[0]*n]
    s=sum(l)
    m=max(l)
    c=l.count(m)
    if 1<c:
        print('no winner')
    elif s<m*2:
        print('majority winner',l.index(m)+1)
    else:
        print('minority winner',l.index(m)+1)