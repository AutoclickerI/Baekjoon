def push(stack,c):
    stack+=c,
    if stack[-3:]==['A','B','B']:
        stack.pop()
        stack.pop()
        stack.pop()
        push(stack,'B')
        stack+='A'

def process(s):
    stack=[]
    for i in s:
        push(stack,i)
    print(*stack,sep='')

for i in[*open(0)][2::2]:
    process(i[:-1])