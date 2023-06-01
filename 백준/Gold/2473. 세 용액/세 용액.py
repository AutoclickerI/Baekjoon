input()
l=sorted(map(int,input().split()))
ptr1,ptr2=0,len(l)-1
ptr3=1
ans=(abs(l[ptr1]+l[ptr2]+l[ptr3]),ptr1,ptr2,ptr3)
for ptr3 in range(1,len(l)):
    ptr1,ptr2=0,len(l)-1
    while ptr1!=ptr2:
        if ptr1!=ptr3!=ptr2:
            if ans[0]>abs(l[ptr1]+l[ptr2]+l[ptr3]):ans=(abs(l[ptr1]+l[ptr2]+l[ptr3]),ptr1,ptr2,ptr3)
            if abs(l[ptr1+1]+l[ptr2]+l[ptr3])<abs(l[ptr1]+l[ptr2-1]+l[ptr3]):ptr1+=1
            else:ptr2-=1
        else:
            ptr1+=(ptr1==ptr3)
            ptr2-=(ptr2==ptr3)
p,q,r=sorted(ans[1:])
print(l[p],l[q],l[r])