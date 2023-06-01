from collections import deque
for i in open(0):
    p,q=i.split()
    dq=deque([(ord(p[0])-97,ord(p[1])-49,0)])
    while 1:
        a,b,c=dq.popleft()
        if a==ord(q[0])-97 and b==ord(q[1])-49:
            print('To get from',p,'to',q,'takes',c,'knight moves.')
            break
        for i in-1,1:
            for j in-2,2:
                if 8>a+i>-1<b+j<8:
                    dq.append((a+i,b+j,c+1))
                if 8>b+i>-1<a+j<8:
                    dq.append((a+j,b+i,c+1))