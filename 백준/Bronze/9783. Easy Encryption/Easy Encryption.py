for i in input().split():
    for j in i:
        s=j
        if j.isalpha():n=ord(j)-96;s=f'{n+58*(n<1):02d}'
        if j.isdigit():s='#'+j
        print(end=s)
    print(end=' ')