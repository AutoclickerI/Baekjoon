I=input
P=print
for T in range(int(I())):P(f'Scenario #{T+1}:');l=eval('input(),'*int(I()));exec("P(''.join(l[int(i)]for i in I().split()[1:]));"*int(I()));P()