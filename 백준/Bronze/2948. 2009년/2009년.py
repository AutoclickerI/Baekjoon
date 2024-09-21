from datetime import*
print('Monday Tuesday Wednesday Thursday Friday Saturday Sunday'.split()[date(2009,*map(int,input().split()[::-1])).weekday()])