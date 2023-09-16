H=1
C=12
N=14
O=16
s=input()
for i in'HCNO':s=s.replace(i,f'+{i}')
for i in range(10):s=s.replace(str(i),f'*{i}')
print(eval(s))