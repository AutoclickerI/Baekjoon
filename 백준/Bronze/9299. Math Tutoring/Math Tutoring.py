for i in range(int(input())):
    n,*l=map(int,input().split())
    print(f'Case {i+1}:',n-1,*[i*j for i,j in zip(l,range(n,0,-1))])