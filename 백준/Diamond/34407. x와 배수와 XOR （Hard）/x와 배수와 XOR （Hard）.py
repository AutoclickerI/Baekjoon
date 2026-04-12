def getk(x):
    while ~x%2:x>>=1
    
    bl=x.bit_length()
    mask=2**bl-2
    
    ans=2**bl
    
    v={0:0}
    b=[0]
    for i in range(1,bl):
        tmpv={}
        tmpb=[]
        mask^=1<<i
        if x&1<<i:
            for j in b:
                if j&1<<i:
                    one=j+(x<<i)&mask
                    if one in tmpv:
                        tmpv[one]=min(tmpv[one],v[j]+(1<<i))
                    else:
                        tmpv[one]=v[j]+(1<<i)
                        tmpb+=one,
                    if one&x<1:
                        ans=min(ans,v[j]+(1<<i))
                else:
                    zero=j&mask
                    if zero in tmpv:
                        tmpv[zero]=min(tmpv[zero],v[j])
                    else:
                        tmpv[zero]=v[j]
                        tmpb+=zero,
                    if j and zero&x<1:
                        ans=min(ans,v[j])
        else:
            for j in b:
                one=j+(x<<i)&mask
                zero=j&mask
                if one in tmpv:
                    tmpv[one]=min(tmpv[one],v[j]+(1<<i))
                else:
                    tmpv[one]=v[j]+(1<<i)
                    tmpb+=one,
                if one&x<1:
                    ans=min(ans,v[j]+(1<<i))
                if zero in tmpv:
                    tmpv[zero]=min(tmpv[zero],v[j])
                else:
                    tmpv[zero]=v[j]
                    tmpb+=zero,
                if j and zero&x<1:
                    ans=min(ans,v[j])
        v=tmpv
        b=tmpb
        if ans<2**bl:
            break
    return ans

for x in[*open(0)][1:]:
    x=int(x)
    if x<1:
        print('1\n2')
    else:
        ans=getk(x)
        print(2)
        print(ans,ans+1)
