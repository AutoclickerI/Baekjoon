for T in[0]*int(input()):
    k=int(input())
    s=[input()for _ in[0]*k]
    r=0
    for i in range(k):
        for j in range(k):
            if i-j:
                ss=s[i]+s[j]
                if ss==ss[::-1]:
                    r=ss
    print(r)