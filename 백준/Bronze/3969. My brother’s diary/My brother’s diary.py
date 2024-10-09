from collections import Counter

for _ in range(int(input())):
    s=input()
    a,*l=Counter(c for c in s if c.isalpha()).most_common()
    if l and a[1]==l[0][1]:
        print("NOT POSSIBLE")
    else:
        d=(ord(a[0])-ord('E'))%26
        print(d,''.join(' '*(c==' ')or chr((ord(c)-d-65)%26+65)for c in s))