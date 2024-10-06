import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def process_recipe(I, C, ingredients):
    result = []
    for w, n, d in ingredients:
        # 전체 양을 분수로 변환
        total_numerator = w * d + n
        total_denominator = d
        
        # 배수 C를 곱함
        total_numerator *= C
        
        # 정수 부분과 분수 부분을 다시 나누기
        whole_part = total_numerator // total_denominator
        fractional_numerator = total_numerator % total_denominator
        fractional_denominator = total_denominator
        
        # 분수가 있다면 기약분수로 나타냄
        if fractional_numerator > 0:
            g = gcd(fractional_numerator, fractional_denominator)
            fractional_numerator //= g
            fractional_denominator //= g
            result.append(f"{whole_part} {fractional_numerator}/{fractional_denominator}")
        else:
            result.append(f"{whole_part}")
    
    return result

def main():
    K = int(input())  # 데이터 세트의 수
    for data_set_number in range(1, K + 1):
        I, C = map(int, input().split())
        ingredients = []
        
        for _ in range(I):
            ingredient_input = input().split()
            if len(ingredient_input) == 1:
                w = int(ingredient_input[0])
                n, d = 0, 1  # 분수 부분이 없는 경우
            else:
                w = int(ingredient_input[0])
                n, d = map(int, ingredient_input[1].split('/'))
            
            ingredients.append((w, n, d))
        
        # 결과 계산
        result = process_recipe(I, C, ingredients)
        
        # 출력
        print(f"Data Set {data_set_number}:")
        for line in result:
            print(line)
        print()  # 빈 줄 출력

if __name__ == "__main__":
    main()