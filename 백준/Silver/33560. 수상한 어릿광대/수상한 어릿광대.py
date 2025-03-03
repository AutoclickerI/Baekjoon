class game:
    def __init__(self):
        self.gain_roll=1
        self.gain_time=4
        self.score=0
        self.time=0
    def exit(self):
        if 124<self.score:return 4
        if 94<self.score:return 3
        if 64<self.score:return 2
        if 34<self.score:return 1
        return 0

p=[0]*5
g=game()
input()
for i in input().split():
    if 240<g.time:
        p[g.exit()]+=1
        g=game()
    if i=='1':
        p[g.exit()]+=1
        g=game()
        g.score=-g.gain_roll
        g.time=-g.gain_time
    if i=='2':
        if g.gain_roll==1:
            g.gain_time+=2
        else:
            g.gain_roll=g.gain_roll//2
    if i=='4':
        g.time+=56
    if i=='5':
        g.gain_time=max(g.gain_time-1,1)
    if i=='6':
        g.gain_roll=min(g.gain_roll*2,32)
    g.score+=g.gain_roll
    g.time+=g.gain_time
print(*p[1:])