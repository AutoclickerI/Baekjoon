_,s=open(0)
print(min(s[:s.rfind('B')].count('R'),
          s[:s.rfind('R')].count('B'),
          s[s.find('R'):].count('B'),
          s[s.find('B'):].count('R')))