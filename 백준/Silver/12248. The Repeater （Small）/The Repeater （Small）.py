for I in range(int(input())):
    l=[[*input()]for _ in[0]*int(input())]
    cnt=[]
    try:
        while l[0]:
            cnt+=[[]]
            s=l[0][-1]
            for n in l:
                c=0
                assert n[-1]==s
                while n and n[-1]==s:
                    n.pop()
                    c+=1
                cnt[-1]+=[c]
        for m in l:
            assert m==[]
        print(f'Case #{I+1}:',sum(min(sum(abs(j-k)for j in m)for k in range(1,101))for m in cnt))
    except:
        print(f'Case #{I+1}: Fegla Won')