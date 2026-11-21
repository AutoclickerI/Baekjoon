G,F=map(int,input().split())
for _ in[m:=99]*8**8:m=min(m,G.bit_length()+G.bit_count()-1);G+=F
print(m)