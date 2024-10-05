import sys
input=sys.stdin.readline
def max_influence(n, animals):
    max_pig_influence = 0
    non_pigs = []

    # 각 동물을 순회하며 돼지와 다른 동물을 구분
    for species, influence in animals:
        if species == "pig":
            max_pig_influence = max(max_pig_influence, influence)
        else:
            non_pigs.append(influence)

    # 돼지보다 영향력이 낮은 동물들의 영향력을 모두 더함
    total_influence = max_pig_influence
    for influence in non_pigs:
        if influence < max_pig_influence:
            total_influence += influence

    return total_influence

# 입력 처리
n = int(input())
animals = [input().split() for _ in range(n)]
animals = [(species, int(influence)) for species, influence in animals]

# 최대 영향력 출력
print(max_influence(n, animals))