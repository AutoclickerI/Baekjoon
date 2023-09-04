while'1'<(s:=input()):
    p,q,r,*s=map(eval,s.split())
    if p<=4.5<150<=q and 200<=r:
        s+='Wide Receiver',
    if p<=6<300<=q and 500<=r:
        s+='Lineman',
    if p<=5<200<=q and 300<=r:
        s+='Quarterback',
    print(*s or['No positions'])