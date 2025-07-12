from datetime import*
a,b=input().split()
print(date.fromisoformat(a)+timedelta(int(b)-1))