for i in[0]*int(input()):
    i=input()
    print(i)
    print(+(len(i)<2*sum(i.count(j)for j in'aeiou')))