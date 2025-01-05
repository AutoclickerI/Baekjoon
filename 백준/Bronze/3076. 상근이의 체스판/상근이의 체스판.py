r,c,a,b=map(int,open(0).read().split())
for i in range(r*a):print(''.join('X.'[j//b-i//a&1]for j in range(c*b)))