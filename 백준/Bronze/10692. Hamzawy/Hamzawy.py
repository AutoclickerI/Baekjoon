for t in range(int(input())):
    s=input()
    n=len(s)
    p=-1
    for i in range(1,n//3+1):
        if s[:i]==s[n-i:]:p=[p,d:=s[:i]][d in s[i:n-i]]
    print(f'Case {t+1}:',p)
