class node:
    def __init__(self,c):
        self.c=c
        self.prev=self
        self.next=self

for*i,_ in[*open(0)][1:]:
    root=n=node('')
    nil=e=node('')
    n.next=e
    e.prev=n
    for c in i:
        if c=='<':
            n=n.prev
        elif c=='>':
            n=n.next
            if n==nil:
                n=n.prev
        elif c=='-':
            if n not in[root,nil]:
                t=n.next,n.prev
                n.prev.next,n.next.prev=t
                n=t[1]
        else:
            v=node(c)
            v.prev=n
            v.next=n.next
            n.next.prev=v
            n.next=v
            n=v
    while root.next!=root:print(end=root.c);root=root.next
    print()