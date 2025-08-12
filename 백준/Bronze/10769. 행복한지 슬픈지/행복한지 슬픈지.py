h,s=map(input().count,(':-)',':-('))
if h+s:
    if s<h:print('happy')
    elif h<s:print('sad')
    else:print('unsure')
else:print('none')