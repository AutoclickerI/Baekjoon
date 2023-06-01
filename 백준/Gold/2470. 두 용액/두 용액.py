input()
l=sorted(map(int,input().split()))
ptr1,ptr2=0,len(l)-1
ans=(abs(l[ptr1]+l[ptr2]),ptr1,ptr2)
while ptr1!=ptr2:
    if ans[0]>abs(l[ptr1]+l[ptr2]):ans=(abs(l[ptr1]+l[ptr2]),ptr1,ptr2)
    if abs(l[ptr1+1]+l[ptr2])<abs(l[ptr1]+l[ptr2-1]):ptr1+=1
    else:ptr2-=1
print(l[ans[1]],l[ans[2]])