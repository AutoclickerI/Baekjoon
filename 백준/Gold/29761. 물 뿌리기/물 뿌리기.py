N,X,x,y=map(int,input().split())
h=[[*map(int,input().split())]for _ in[0]*N]
from heapq import heappush,heappop
water=[N*[0]for _ in[0]*N]
water[x-1][y-1]=X
hq=[(-h[x-1][y-1],-X,x-1,y-1)]

def simulate(y,x,v):
    if 1<v:
        for dy,dx in(-1,0),(0,1),(1,0),(0,-1):
            if 0<=y+dy<N>x+dx>=0:
                if h[y+dy][x+dx]<h[y][x]:
                    if water[y+dy][x+dx]<X:
                        water[y+dy][x+dx]=X
                        heappush(hq,(-h[y+dy][x+dx],-X,y+dy,x+dx))
                elif h[y+dy][x+dx]==h[y][x] and water[y+dy][x+dx]<v-1:
                    water[y+dy][x+dx]=v-1
                    heappush(hq,(-h[y+dy][x+dx],1-v,y+dy,x+dx))

while hq:
    _,_,y,x=heappop(hq)
    simulate(y,x,water[y][x])

print(sum(i>0 for j in water for i in j))