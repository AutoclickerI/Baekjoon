from itertools import*

def backtrack(n):
    global flag
    if n==15:
        flag|=v==arr
        return
    s,e=g[n]
    for i in 0,1,2:
        if v[s*3+i]<arr[s*3+i]and v[e*3+2-i]<arr[e*3+2-i]:
            v[s*3+i]+=1
            v[e*3+2-i]+=1
            backtrack(n+1)
            v[s*3+i]-=1
            v[e*3+2-i]-=1
            
*g,=combinations(range(6),2)
for i in open(0):
    flag=0
    *arr,=map(int,i.split())
    v=[0]*18
    backtrack(0)
    print(flag)