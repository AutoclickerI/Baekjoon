for T in range(int(input())):
    a=0
    n=int(input())
    s,f=map(int,input().split())
    for _ in[0]*n:S,F,r=map(int,input().split());a+=r*max(1-max(s,S)+min(f,F),0)
    print(f'Data Set {T+1}:\n{a}\n')