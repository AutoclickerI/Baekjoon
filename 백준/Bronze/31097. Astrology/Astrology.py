_,q,r=map(int,input().split('-'))
n=q*30+r
if 381<n or n<50:
    s='Capricorn'
elif n<79:
    s='Aquarius'
elif n<111:
    s='Pisces'
elif n<140:
    s='Aries'
elif n<171:
    s='Taurus'
elif n<201:
    s='Gemini'
elif n<233:
    s='Cancer'
elif n<263:
    s='Leo'
elif n<293:
    s='Virgo'
elif n<323:
    s='Libra'
elif n<353:
    s='Scorpio'
else:
    s='Sagittarius'
print(s)