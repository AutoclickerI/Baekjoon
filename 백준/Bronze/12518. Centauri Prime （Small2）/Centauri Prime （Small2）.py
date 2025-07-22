for T in range(int(input())):
    s=input()
    c=s[-1].lower()
    print(f'Case #{T+1}: {s} is ruled by {"nobody"if c=="y"else"a queen"if c in"aeiou"else"a king"}.')