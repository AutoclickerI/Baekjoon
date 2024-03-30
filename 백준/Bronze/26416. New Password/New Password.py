for i in range(int(input())):
    input()
    S=input()
    if 1-any(i.isupper()for i in S):
        S+='A'
    if 1-any(i.islower()for i in S):
        S+='a'
    if 1-any(i.isdigit()for i in S):
        S+='1'
    if not{*S}&{*'#@*&'}:
        S+='#'
    print(f'Case #{i+1}:',(S+'1'*6)[:max(len(S),7)])