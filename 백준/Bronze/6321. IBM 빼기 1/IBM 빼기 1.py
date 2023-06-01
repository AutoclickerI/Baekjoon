for j in range(int(input())):
    l=[chr(ord(i)+1 if ord(i)<90 else 65)for i in input()]
    print(f'String #{j+1}\n{"".join(l)}\n')