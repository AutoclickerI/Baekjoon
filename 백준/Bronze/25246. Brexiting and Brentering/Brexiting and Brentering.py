s=input()
print(s[:max(s.rfind(c)for c in'aeiou')+1]+'ntry')