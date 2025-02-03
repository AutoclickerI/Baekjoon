n,m=sorted(map(int,input().split()))
right = True
answer = 0
for i in range(1, 1440):
    if i % n == 0 == i % m:
        answer += 1
        right = not right
    elif i % n == 0 and not right:
        answer += 1
        right = True
    elif i % m == 0 and right:
        answer += 1
        right = False
print(answer)