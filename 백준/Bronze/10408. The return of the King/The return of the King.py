S=input()
z=S.count('0')
print(f'{(sum(map(int,S))+9*z)/(len(S)-z):.2f}')