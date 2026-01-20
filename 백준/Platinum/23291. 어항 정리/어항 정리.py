N,K,*l=map(int,open(0).read().split())

def update(arr):
    t=[[0]*len(i)for i in arr]
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            for dy,dx in(-1,0),(1,0),(0,1),(0,-1):
                ny,nx=y+dy,x+dx
                if 0<=ny<len(arr)and 0<=nx<len(arr[ny])and 4<arr[y][x]-arr[ny][nx]:
                    mv=(arr[y][x]-arr[ny][nx])//5
                    t[y][x]-=mv
                    t[ny][nx]+=mv
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            arr[y][x]+=t[y][x]

def rot90(arr):
    return[[*i][::-1]for i in zip(*arr)]
c=0
while K<max(l)-min(l):
    c+=1
    mv=min(l)
    for i in range(N):
        if l[i]==mv:l[i]+=1
    roll=[l[:1]]
    l=l[1:]
    while len(roll)<=len(l):
        roll=rot90(roll)
        roll+=l[:len(roll[0])],
        l=l[len(roll[0]):]
    roll[-1]+=l
    update(roll)
    l=[]
    for i in zip(*roll):
        l+=i[::-1]
    l+=roll[-1][len(roll[0]):]
    roll=[l[N//2:N-N//4][::-1],l[N//4:N//2],l[:N//4][::-1],l[N-N//4:]]
    update(roll)
    l=[]
    for i in zip(*roll):
        l+=i[::-1]
print(c)