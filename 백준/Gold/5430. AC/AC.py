from collections import deque
for _ in[0]*int(input()):
    c=input()
    input()
    l=deque(eval(input()))
    f=0
    try:
        for i in c:
            if i=='R':
                f^=1
            else:
                if f:
                    l.pop()
                else:
                    l.popleft()
        l=[*l]
        if f:
            l=l[::-1]
        print(*str(l).split(),sep='')
    except:
        print('error')