a=[int(input())for i in range(3)]
a.sort()
print('Error'if sum(a)!=180 else'Equilateral'if a[0]==a[2]else'Scalene'if a[0]!=a[1]!=a[2]else'Isosceles')