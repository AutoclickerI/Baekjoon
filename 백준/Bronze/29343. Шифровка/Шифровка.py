def solve():
    import sys
    input = sys.stdin.readline
    
    n = int(input().strip())
    s = input().strip()
    
    vowels = set("aeiouAEIOU")
    
    # Префиксная сумма: для каждой позиции считаем число гласных от начала до этой позиции.
    prefix_vowels = [0] * (n + 1)
    for i in range(n):
        prefix_vowels[i+1] = prefix_vowels[i] + (1 if s[i] in vowels else 0)
    
    # Суффиксная сумма: для каждой позиции считаем число гласных от этой позиции до конца строки.
    suffix_vowels = [0] * (n + 1)
    for i in range(n-1, -1, -1):
        suffix_vowels[i] = suffix_vowels[i+1] + (1 if s[i] in vowels else 0)
    
    count = 0
    # Перебираем все возможные длины k от 1 до n
    for k in range(1, n + 1):
        # Префикс k: s[0:k] - число гласных = prefix_vowels[k]
        # Суффикс k: s[n-k:n] - число гласных = suffix_vowels[n-k]
        pv = prefix_vowels[k]
        sv = suffix_vowels[n - k]
        if pv == sv and pv != 0:
            count += 1
            
    print(count)

if __name__ == '__main__':
    solve()
