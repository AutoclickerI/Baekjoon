for T in range(int(input())):
 print(f'Scenario #{T+1}:')
 l=eval('input(),'*int(input()))
 for _ in[0]*int(input()):print(''.join(l[int(i)]for i in input().split()[1:]))
 print()