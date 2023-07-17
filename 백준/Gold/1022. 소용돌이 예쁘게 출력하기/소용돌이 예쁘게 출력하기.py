r1,c1,r2,c2=map(int,input().split())
def get_num(i,j):
    if i==j:
        return(i+j+1)**2 if i>0 else (i+j)**2+1
    if i==-j:
        return (i-j)**2-i+j+1 if i>0 else (i-j)**2-i+j+1
    if abs(i)>abs(j):
        if i>0:
            return get_num(i,-i)-i-j
        else:
            return get_num(i,i)-i+j
    else:
        if j>0:
            return get_num(-j,j)+i+j
        else:
            return get_num(j,j)-i+j
l=[[str(get_num(i,j))for i in range(c1,c2+1)]for j in range(r1,r2+1)]
m=max(max(len(i)for i in j)for j in l)
l=[[' '*(m-len(i))+i for i in j]for j in l]
[print(*i)for i in l]