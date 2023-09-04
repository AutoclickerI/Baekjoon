for i in range(int(input())):
    print(f'Case {i+1}:')
    n=int(input())
    for i in range(1,n//2+1):
        if n-i<7:
            print(f'({i},{n-i})')