l=input().split()[::-1]
a=[]
def exec_statement():
    global a,l
    t=l.pop()
    if t=='{':
        a+=t
        while t!='}':
            t=l.pop()
            if t=='if':
                l+=t,
                exec_structure()
            else:
                a+=t,
    else:
        a+='{'
        if t=='if':
            l+=t,
            exec_structure()
        else:
            a+=t,
        a+='}'
        
    
    
def exec_structure():
    global a,l
    t=l.pop()
    if t!='if':
        a+=t,
        return
    a+=t,
    exec_statement()
    if l and (t:=l.pop())=='else':
        a+=t,
        exec_statement()
    else:
        l+=t,

while l:
    exec_structure()
print(*a)