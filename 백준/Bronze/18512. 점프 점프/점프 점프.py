x,y,a,b=map(int,input().split())
r=range(7**6)
print(min({*r[a::x]}&{*r[b::y]}or[-1]))