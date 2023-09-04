for i in[*open(0)][:-1]:
    p,q,r,s=map(int,i.replace(*': ').split())
    t,h=divmod((p+r)*60+q+s,1440)
    print(f'{h//60:02}:{h%60:02}'+f' +{t}'*min(t,1))