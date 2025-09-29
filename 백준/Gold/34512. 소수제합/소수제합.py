N=int(input())
if N<3:
    print(-1)
elif N<4:
    print(2,5,29)
elif N<5:
    print(2,2,3,17)
elif N==6:
    print(2,2,3,3,3,5)
else:
    print(*'2'*(6-N%2*3)+'3'*(N-6+N%2*3))