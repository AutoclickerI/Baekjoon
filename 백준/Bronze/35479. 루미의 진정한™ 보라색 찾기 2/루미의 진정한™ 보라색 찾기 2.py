R,G,B=map(int,input().split())
K=(255-max(R,G,B))
if K==255:
    print(0,0,0,1)
else:
    print((255-R-K)/(255-K),(255-G-K)/(255-K),(255-B-K)/(255-K),K/255)