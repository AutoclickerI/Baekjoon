s=input()
print(min((s*2)[i:i+s.count('a')].count('b')for i in range(len(s))))