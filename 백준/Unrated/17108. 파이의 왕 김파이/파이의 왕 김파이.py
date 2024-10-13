N,L,R,*l=map(int,open(0).read().split())
l=[*l,*[0]*N][:N]

def check(length):
    ans=0
    acc=0
    for i in l:
        if i==0:
            ans+=length+length*(acc>0)
            acc=0
        elif acc+i<=length:
            acc+=i
        else:
            ans+=length
            acc=i
    return ans+length*(acc>0)

print(min(check(i)for i in range(L,R+1)))