try:
    while 1:
        l=[[0]*31,[0]*31]
        for _ in[0]*int(input()):
            M,L=input().split();l[L=='E'][int(M)-30]+=1
        print(sum(map(min,zip(*l))))
except:0