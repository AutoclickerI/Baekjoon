N=int(input())
v=1
while 2**v<=N:v*=2
print(v,'bits'[:v*3])