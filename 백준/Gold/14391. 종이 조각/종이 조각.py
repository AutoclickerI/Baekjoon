_,*l=[i[:-1]for i in open(0)]

def f(arr):
    if len(arr)==0:return 0
    if len(arr)==len(arr[0])==1:
        return int(arr[0][0])
    *ta,=zip(*arr)
    return max([max(f(i[:j])+int(''.join(i[j]))+f(i[j+1:])for j in range(len(i)))for i in[arr,ta]])

print(max(f(l),f([*zip(*l)])))