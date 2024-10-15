a,n=0,1
while 1:
    print('?',1,n);s=input()
    if 'A'<s:break
    a=max(a,int(s));n+=1
for i in range(2,n):
    for j in range(1,n):print('?',i,j);a=max(a,int(input()))
print('!',a)