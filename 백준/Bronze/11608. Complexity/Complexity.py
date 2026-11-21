S=input()
print(sum(sorted(map(S.count,{*S}))[:-2]))