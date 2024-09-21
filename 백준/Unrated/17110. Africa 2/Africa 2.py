import random
dic={'botswana': 0, 'ethiopia': 50, 'kenya': 50, 'south-africa': 0, 'tanzania': 50, 
     'namibia': 140, 'zambia':50, 'zimbabwe':30}
case1=['zambia','zimbabwe']
ans=0
cache=0
flag=0
for i in range(int(input())):
    a=input()
    if a in case1 and cache in case1:
        ans-=dic[cache]
        ans+=50
        continue
    if a=='south-africa':
        flag = 1
    if a=='namibia':
        if flag:
            ans+=40
            continue
    ans+=dic[a]
    cache=a
random.seed(cache)
print(ans if ans==0 else ans if round(random.random(),2)in[0.06,0.43] else ans if cache in ['ethiopia','south-africa','tanzania','namibia']else -1)