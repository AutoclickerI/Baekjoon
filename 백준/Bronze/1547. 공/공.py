ball='1'
for i in[0]*int(input()):
    l=input().split()
    if ball in l:
        del l[l.index(ball)]
        ball=l.pop()
print(ball)