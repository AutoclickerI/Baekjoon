s=input()
n=int(input())
tmp=[sorted(s[i::n])for i in range(n)]
i=0
while 1:
    for j in tmp:
        if i==len(j):
            exit()
        print(end=j[i])
    i+=1