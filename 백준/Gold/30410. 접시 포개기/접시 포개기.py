input()
prev1=cur1=cur2=m=0
for i in input().split():
    if i=='1':
        cur1+=1
    else:
        if cur1%2:
            prev1=cur1
            cur2=1
        else:
            cur2+=cur1//2+1
        cur1=0
    m=max(m,(prev1//2+cur1//2+cur2).bit_length())
print(1<<m)