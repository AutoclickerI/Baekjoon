while True:
    a,b,c,d=arr=[*map(int,input().split())]
    if a==b==c==d==-1:break
    ans=-1;idx=arr.index(-1)
    for tr in range(1,10001):
        arr[idx]=tr
        a,b,c,d=arr
        if (b*b==a*c and c*c==b*d) or b-a==c-b==d-c:
            ans=tr
    print(ans)