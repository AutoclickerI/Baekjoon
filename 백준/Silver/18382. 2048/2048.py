n=int(input())
s=input()
b=[[*i]for i in zip(*[map(int,input().split())]*4)]

def R(arr):
    global n
    arr=[i for i in arr if i]
    for i in range(len(arr)-1)[::-1]:
        if arr[i]==arr[i+1]:
            n+=arr[i]*2
            arr[i]=0
            arr[i+1]*=2
    return([0]*4+[i for i in arr if i])[-4:]

for d,v,y,x in zip(*[iter(s)]*4):
    if d=='L':
        b=[R(i[::-1])[::-1]for i in b]
    if d=='R':
        b=[R(i)for i in b]
    if d=='D':
        b=[[*i]for i in zip(*map(R,zip(*b)))]
    if d=='U':
        b=[[*i]for i in zip(*[R(i[::-1])[::-1]for i in zip(*b)])]
    b[int(y)][int(x)]=int(v)

print(n)