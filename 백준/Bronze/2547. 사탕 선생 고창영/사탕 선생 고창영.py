for _ in[0]*int(input()):
    input()
    n=int(input())
    l=0
    for __ in[0]*n:
        l+=int(input())
    print('YNEOS'[l%n!=0::2])