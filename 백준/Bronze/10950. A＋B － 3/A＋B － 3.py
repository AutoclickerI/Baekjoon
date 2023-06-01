n = int(input())
list1 = []
for i in range(n):
    list1.append(input().split(' '))
for i in range(n):
    print(int(list1[i][0]) + int(list1[i][1]))