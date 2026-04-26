N=int(input())
arr=[N*10*[' ']for _ in[0]*2*N]

for i in range(N*2):
    arr[~i][i]='*'
mr=0
for y in range(N):
    arr[y][3*N-y]=arr[y][3*N-y+2+y*2]=arr[~y][3*N-y]=arr[~y][3*N-y+2+y*2]='*'
    mr=max(mr,3*N-y+2+y*2)
for i in arr:print(''.join(i)[:mr+1])