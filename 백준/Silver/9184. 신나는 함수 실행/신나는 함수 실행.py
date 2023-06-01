w_li = {} #값 저장
 
def w(a,b,c):
    if (a,b,c) in w_li:
        return w_li[(a,b,c)]
    
    else:
        if a <= 0 or b <= 0 or c <= 0:
            w_li[(a,b,c)] = 1
            return 1
 
        if a > 20 or b > 20 or c > 20:
            w_li[(a,b,c)] = w(20, 20, 20)
            return w(20, 20, 20)
 
        if a < b and b < c:
            w_li[(a,b,c)] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
            return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
 
        else:
            w_li[(a,b,c)] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
 
            return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
 
while(1):
    a,b,c = map(int,input().split())
    if a==-1 and b==-1 and c==-1:
        break
    else:
        print("w(%d, %d, %d) = %d"%(a,b,c,w(a,b,c)))