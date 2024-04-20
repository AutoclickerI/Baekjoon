#https://www.acmicpc.net/board/view/141460 답변용 코드

from collections import deque



def roundUp(x):
    if (x - int(x)) >= 0.5:
        return int(x) + 1
    else:
        return int(x)


# 첫 줄에 난이도 의견의 개수 n이 주어진다.
level = int(input())

# 두 번째 줄부터 1 + n번째 줄까지 사용자들이 제출한 난이도 의견 n개가 한 줄에
# 하나씩 주어진다. 모든 난이도 의견은 1 이상 30이하 이다.
levels = deque([])
for i in range(level):
    number = int(input())
    levels.append(number)

# 등록된 난이도 배열을 정렬시키기
# 단, deque는 따로 정렬 기능이 없기 때문에 리스트로 변환하고
# 당렬하면 다시 큐로 바꾸기
tempList = list(levels)
tempList.sort()
sorted_deque = deque(tempList)

# 등록된 난이도 의견 수 에서 30% 곱하기
avrArr = len(sorted_deque) * 0.15

# 곱해진 결과를 반올림 하기
firstResult = roundUp(avrArr)

# 반올림 된 수 만큼 배열의 양쪽에서 제외시키기
# 내 생각엔 큐를 써야할 것 같음.
for i in range(firstResult):
    if sorted_deque:
        sorted_deque.popleft()
    if sorted_deque:
        sorted_deque.pop()


# 제외 시킨 배열의 평균 구하기
sumLevels = sum(sorted_deque)
if len(sorted_deque) > 0:
    #avr = sumLevels / len(sorted_deque)
    avr = (sumLevels+len(sorted_deque)//2) // len(sorted_deque)
else:
    avr = 0


# 결과 값 반올림 하기
#secondResult = roundUp(avr)

# 출력하기
print(avr)