def leftpossible(string,s,e):
    cnt=0
    for i in range(s,e+1):
        if string[i]==')':cnt-=1
        elif string[i]=='*':return True
        else:cnt+=1
        if cnt<0:return False
    return True

def rightpossible(string,s,e):
    cnt=0
    for i in range(e,s-1,-1):
        if string[i]=='(':cnt-=1
        elif string[i]=='*':return True
        else:cnt+=1
        if cnt<0:return False
    return True

def check(string):
    cnt=0
    qmark=0
    for i in range(len(string)):
        if string[i]=='(':
            cnt+=1
        if string[i]==')':
            cnt-=1
        if string[i]=='?':
            qmark+=1
        if string[i]=='*':
            return leftpossible(string,0,i-1)and rightpossible(string,i+1,len(string)-1)
        if cnt<0:
            qmark-=1
            cnt+=1
        if qmark<0:
            return False
    if cnt>qmark:
        return False
    if cnt==qmark:
        return string[-1]!='('
    if cnt<qmark:
        return(qmark-cnt)%2==0 and string[-1]!='('
for _ in range(int(input())):
    s=input()
    if check(s)and check(s[::-1].replace(*'(.').replace(*')(').replace(*'.)')):
        print('YES')
    else:
        print('NO')