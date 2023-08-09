from datetime import*
for i in[*open(0)][1:]:
    p,q=map(int,i.split())
    d=datetime(p,q,q)-timedelta(days=q)
    print(d.year,d.month,d.day)