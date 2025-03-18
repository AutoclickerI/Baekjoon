N=int(input())
edge=[0]*N

for _ in[0]*N:
    n,l,r=map(ord,input()[::2])
    edge[n-65]=[l-65,r-65]

def preorder(n):
    if n<0:
        return
    print(end=chr(n+65))
    [*map(preorder,edge[n])]

def inorder(n):
    if n<0:
        return
    inorder(edge[n][0])
    print(end=chr(n+65))
    inorder(edge[n][1])

def postorder(n):
    if n<0:
        return
    [*map(postorder,edge[n])]
    print(end=chr(n+65))

preorder(0)
print()
inorder(0)
print()
postorder(0)