def left_append(st,s):
    if s<1 or st[s-1]=='(':
        return s
    else:
        cnt=1
        ret=s-2
        while cnt and 0<=ret:
            if st[ret]==')':
                cnt+=1
            else:
                cnt-=1
            ret-=1
        if cnt:
            return s
        else:
            return ret+1
def right_append(st,e):
    if e+1>=len(st) or st[e+1]==')':
        return e
    else:
        cnt=1
        ret=e+2
        while cnt and ret<len(st):
            if st[ret]=='(':
                cnt+=1
            else:
                cnt-=1
            ret+=1
        if cnt:
            return e
        else:
            return ret-1
def both_append(st,s,e):
    if e+1>=len(st) or s<1:
        return s,e
    if st[e+1]==')':
        if st[s-1]=='(':
            return s-1,e+1
        else:
            tmp=s
            while 1:
                tmp2=left_append(st,tmp)
                if tmp==tmp2:
                    return s,e
                elif 0<tmp2 and st[tmp2-1]=='(':
                    return tmp2,e
                tmp=tmp2
    if st[s-1]=='(':
        tmp=e
        while 1:
            tmp2=right_append(st,tmp)
            if tmp==tmp2:
                return s,e
            elif tmp2+1<len(st) and st[tmp2+1]==')':
                return s,tmp2
            tmp=tmp2
    return s,e
def solve(st,mid):
    s=mid
    e=mid+1
    if st[s:e+1]=='()':
        return True
    if st[s:e+1]=='((':
        cnt=1
        while cnt and e<len(st):
            if st[e]=='(':
                cnt+=1
            else:
                cnt-=1
            e+=1
        if cnt:
            return
        else:
            e-=1
    elif st[s:e+1]=='))':
        cnt=1
        while cnt and 0<=s:
            if st[s]==')':
                cnt+=1
            else:
                cnt-=1
            s-=1
        if cnt:
            return
        else:
            s+=1
    elif st[s:e+1]==')(':
        cnt=1
        e+=1
        while cnt and e<len(st):
            if st[e]=='(':
                cnt+=1
            else:
                cnt-=1
            e+=1
        if cnt:
            return
        else:
            e-=1
        
        cnt=1
        s-=1
        while cnt and 0<=s:
            if st[s]==')':
                cnt+=1
            else:
                cnt-=1
            s-=1
        if cnt:
            return
        else:
            s+=1
    while 0<=s and e<N:
        flag=False
        if mid-s+1==e-mid:
            return True
        elif mid-s+1<e-mid:
            tmp=left_append(st,s)
            if tmp<s:
                s=tmp
            else:
                flag=True
        else:
            tmp=right_append(st,e)
            if e<tmp:
                e=tmp
            else:
                flag=True
        if flag:
            tmp=both_append(st,s,e)
            if (s,e)==tmp:
                return
            s,e=tmp
            
N=int(input())
if N%2==0:
    print('junhui')
else:
    s=input()
    if solve(s,N//2) or solve(s,N//2-1):
        print('jimin')
    else:
        print('junhui')