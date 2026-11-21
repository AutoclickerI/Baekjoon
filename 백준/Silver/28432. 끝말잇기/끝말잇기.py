l=[input()for _ in range(int(input()))]
i=l.index('?')
w=[input()for _ in range(int(input()))]
s={*l}
def check(li):
    for i,j in zip(li,li[1:]):
        if i[-1]!=j[0]:return 0
    return 1
for word in w:
    l[i]=word
    if word not in s and check(l):print(word)