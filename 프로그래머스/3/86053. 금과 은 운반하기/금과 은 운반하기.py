def solution(a, b, g, s, w, t):
    def simulate(n):
        ss=gg=tot=0
        for i in range(len(g)):
            cnt=(n+t[i])//2//t[i]
            ss+=min(s[i],w[i]*cnt)
            gg+=min(g[i],w[i]*cnt)
            tot+=min(s[i]+g[i],w[i]*cnt)
        return a<=gg and b<=ss and a+b<=tot
    ss=0
    ee=10**15
    while 1<ee-ss:
        m=ss+ee>>1
        if simulate(m):
            ee=m
        else:
            ss=m
    return ee