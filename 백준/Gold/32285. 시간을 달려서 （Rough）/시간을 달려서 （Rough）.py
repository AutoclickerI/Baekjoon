G,F=map(int,input().split())
m=100
while G.bit_length()-1<m:m=min(m,G.bit_length()+G.bit_count()-1);G+=F
print(m)