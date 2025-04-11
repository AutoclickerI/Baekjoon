N=int(input())

def move_count(n):
    if n==1:
        return 1
    else:
        return move_count(n-1)*2+1

print(move_count(N))

# start 기둥에 있는 원판을 end 기둥으로 옮김. 이때 옮기는 원판의 개수는 count개
def move(start,end,count):
    if count==1:
        print(start,end)
    else:
        remain=6-start-end
        move(start,remain,count-1)
        print(start,end)
        move(remain,end,count-1)

if N<=20:
    move(1,3,N)