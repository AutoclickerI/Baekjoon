input()
*l1,=map(int,input().split())
*l2,=map(int,input().split())
a=0
for i in l1:
    for j in l2:
        a+=(i>j)-(i<j)
if a>0:
    print('first')
elif a<0:
    print('second')
else:
    print('tie')