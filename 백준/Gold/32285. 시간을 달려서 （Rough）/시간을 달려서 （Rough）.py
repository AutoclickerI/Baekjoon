G,F=map(int,input().split())
f=lambda n:n.bit_length()+n.bit_count()-1
m=f(G)
while G.bit_length()-1<m:
    G+=F
    m=min(m,f(G))
print(m)