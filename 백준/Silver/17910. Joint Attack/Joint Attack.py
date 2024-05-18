*p,a=map(int,[*open(0)][1].split())
b=1
for i in p[::-1]:a,b=b+a*i,a
print(f'{a}/{b}')