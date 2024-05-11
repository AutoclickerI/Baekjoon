for i in open(0):
    if not i[:-1].isdigit()and len(i)<12 and sum(j.isupper()for j in i)<=sum(j.islower()for j in i):
        print(end=i)