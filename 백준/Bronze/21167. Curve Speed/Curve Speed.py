for i in open(0):
    p,q=map(eval,i.split())
    print(round((p*(q+.16)/.067)**.5))