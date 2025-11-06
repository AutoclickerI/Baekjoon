stack=[]
ans=[]
for i in input():
    if i in'()+-*/':
        if i=='*':
            while stack and stack[-1]in'/*':
                ans+=stack.pop()
            stack+='*'
        if i=='/':
            while stack and stack[-1]in'/*':
                ans+=stack.pop()
            stack+='/'
        if i=='+':
            while stack and stack[-1]in'+-/*':
                ans+=stack.pop()
            stack+='+'
        if i=='-':
            while stack and stack[-1]in'+-/*':
                ans+=stack.pop()
            stack+='-'
        if i=='(':
            stack+='('
        if i==')':
            while stack[-1]!='(':
                ans+=stack.pop()
            stack.pop()
    else:
        ans+=i
while stack:
    ans+=stack.pop()
print(*ans,sep='')