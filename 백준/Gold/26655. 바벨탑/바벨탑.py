N=int(input())
l=[int(i)//10-2for i in input().split()]+[0]

stack=[]
s=0
m=0
c=0
for i in l:
    if s<=i:
        stack+=i-s,
        s=i
    else:
        while i<s:
            p=stack.pop()
            m+=2*p
            s-=p
            if s<=i:
                stack+=i-s,
                m-=(i-s)*2
                p-=i-s
                s=i
            c-=p//-4
print(m*10,c*4)