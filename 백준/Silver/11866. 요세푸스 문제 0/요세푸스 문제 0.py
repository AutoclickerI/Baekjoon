p,q=list(map(int,input().split()))
l=q
q-=1
n=list(range(1,p+1))
b=[]
try:
    while True:
        b.append(n[q])
        del n[q]
        q+=l-1
        q%=len(n)
except:
    print(f'<{b[0]}',end='');[print(f', {b[i]}',end='')for i in range(1,len(b))];print('>')