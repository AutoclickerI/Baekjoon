N,M,Q=map(int,input().split())
price=[[*map(int,input().split())]for _ in[0]*N]
query=[[*map(int,input().split())]for _ in[0]*Q]
price_sum=[0]
for p,_ in price:
    price_sum+=price_sum[-1]+p,
*N_price,=eval('[[-1,0]],'*-~M)
for i,[p,m]in enumerate(price):
    N_price[m]+=[i,N_price[m][-1][1]+p//2],
from bisect import*
for m,s,e in query:
    print(price_sum[e]-price_sum[s-1]-N_price[m][bisect_left(N_price[m],[e,0])-1][1]+N_price[m][bisect_left(N_price[m],[s-1,0])-1][1])