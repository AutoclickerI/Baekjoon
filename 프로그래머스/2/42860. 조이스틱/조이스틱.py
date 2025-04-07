def solution(name):
    answer = 0
    for i in name:
        answer+=min(ord(i)-65,91-ord(i))
    
    if answer==0:
        return 0
    
    name_forward=name.rstrip('A')
    name_backward=(name[0]+name[1:][::-1]).rstrip('A')
    
    addr=min(len(name_forward),len(name_backward))-1
    
    s=0
    for i in range(len(name)-1):
        if name[i]=='A'and name[i+1]!='A':
            addr=min(addr,s+s+len(name)-i-1)
        if name[i]!='A'and name[i+1]=='A':
            s=i
    
    name=name[0]+name[1:][::-1]
    
    for i in range(len(name)-1):
        if name[i]=='A'and name[i+1]!='A':
            addr=min(addr,s+s+len(name)-i-1)
        if name[i]!='A'and name[i+1]=='A':
            s=i
    
    return answer+addr