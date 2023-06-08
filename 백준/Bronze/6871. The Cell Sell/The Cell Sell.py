p,q,r=map(int,open(0))
a=max(0,(p-100)*25)+q*15+r*20
b=max(0,(p-250)*45)+q*35+r*25
print(f'Plan A costs {a/100:.2f}')
print(f'Plan B costs {b/100:.2f}')
print(*('Plan','AB'[a>b],'is cheapest.')if a-b else["Plan A and B are the same price."])