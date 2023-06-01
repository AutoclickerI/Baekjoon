c=int(input())
i=1
while c-1:
    c=3*c+1 if c%2 else c//2
    i+=1
print(i)