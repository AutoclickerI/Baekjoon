s=input()
k=s[-2:]
exec(f"print(*[''.join(x*{k}for x in input())]*{k});"*int(s[:2]))