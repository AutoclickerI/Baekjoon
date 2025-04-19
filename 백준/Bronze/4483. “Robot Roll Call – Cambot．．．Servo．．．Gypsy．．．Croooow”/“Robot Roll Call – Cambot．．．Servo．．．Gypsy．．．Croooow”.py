for T in range(int(input())):
    s=eval('input(),'*int(input()));v=sum([input().split()for _ in[0]*int(input())],[]);print(f'Test set {T+1}:')
    for i in s:print(i,'is','parbe'[i not in v::2]+'sent')
    print()