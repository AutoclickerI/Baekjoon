for T in range(int(input())):
    s,n=input().split()
    n=int(n)
    possible=-1
    acc=0
    ans=0
    for i in range(len(s)):
        if s[i] in'aeiou':
            acc=0
        else:
            acc+=1
        if n<=acc:
            possible=i-n+1
        ans+=possible+1
    print(f'Case #{T+1}:',ans)