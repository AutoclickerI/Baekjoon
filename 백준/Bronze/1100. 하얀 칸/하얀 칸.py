a=[input()for i in range(8)];n=0
for i in range(8):
    for j in range(8):
        if a[i][j]!='.'and j%2==i%2:
            n+=1
print(n)