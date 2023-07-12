# https://www.acmicpc.net/board/view/121641 테스트용 코드

from sys import exit, stdin

# 도감 수록 개수 n, 문제 개수 m 입력.
n, m = map(int, input().split())
assert 1 <= n <= 100000
assert 1 <= m <= 100000

poke_dict = {}
for i in range(1, n+1):
    # 포켓몬 이름 name 입력.
    name = stdin.readline().rstrip()
    assert 2 <= len(name) <= 20
    #assert (name[0].isupper() and name[1:].islower()) or (name[-1].isupper() and name[:-1].islower())

    poke_dict[str(i)] = name
    poke_dict[name] = str(i)

for _ in range(m):
    # 문제 question 입력.
    question = stdin.readline().rstrip()

    # 유효한 문제는 응답.
    assert question in poke_dict
    print(poke_dict[question])