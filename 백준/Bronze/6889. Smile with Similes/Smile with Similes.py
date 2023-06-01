n=int(input())
m=int(input())
l=[input()for _ in[0]*n]
m=[input()for _ in[0]*m]
for i in l:
    for j in m:
        print(i,'as',j)