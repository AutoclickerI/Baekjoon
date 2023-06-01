p,q=map(int,input().split())
d={input():1for _ in[0]*p}
l=sorted([i for i in[input()for _ in[0]*q]if d.get(i)])
print(len(l),*l)