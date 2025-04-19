for T in range(1,int(input())+1):
    s=[input()for _ in[0]*int(input())];v=sum([input().split()for _ in[0]*int(input())],[]);print(f'Test set {T}:')
    for i in s:print(i,'is','parbe'[i not in v::2]+'sent')
    print()