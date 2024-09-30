def draw_rectangle(r, c, filled):
    if filled == 'y':
        for i in range(r):
            print('#' * c)
    else:
        for i in range(r):
            if i == 0 or i == r - 1:
                print('#' * c)
            else:
                print('#' + ' ' * (c - 2) + '#')

def draw_left_triangle(s, filled):
    if filled == 'y':
        for i in range(1, s + 1):
            print('#' * i)
    else:
        for i in range(1, s + 1):
            if i == 1 or i == s:
                print('#' * i)
            else:
                print('#' + ' ' * (i - 2) + '#')

def draw_right_triangle(s, filled):
    if filled == 'y':
        for i in range(1, s + 1):
            print(' ' * (s - i) + '#' * i)
    else:
        for i in range(1, s + 1):
            if i == 1 or i == s:
                print(' ' * (s - i) + '#' * i)
            else:
                print(' ' * (s - i) + '#' + ' ' * (i - 2) + '#')

def draw_diamond(s, filled):
    mid = s // 2
    if filled == 'y':
        for i in range(mid):
            print(' ' * (mid - i) + '#' * (2 * i + 1))
        for i in range(mid, -1, -1):
            print(' ' * (mid - i) + '#' * (2 * i + 1))
    else:
        for i in range(mid):
            if i == 0:
                print(' ' * (mid - i) + '#')
            else:
                print(' ' * (mid - i) + '#' + ' ' * (2 * i - 1) + '#')
        print('#'+' '*(s-2)+'#')
        for i in range(mid - 1, -1, -1):
            if i == 0:
                print(' ' * (mid - i) + '#')
            else:
                print(' ' * (mid - i) + '#' + ' ' * (2 * i - 1) + '#')

# 입력 받기
n = int(input())
for _ in range(n):
    data = input().split()
    shape = data[0]
    if shape == "rectangle":
        r = int(data[1])
        c = int(data[2])
        filled = data[3]
        draw_rectangle(r, c, filled)
    elif shape == "left":
        s = int(data[2])
        filled = data[3]
        draw_left_triangle(s, filled)
    elif shape == "right":
        s = int(data[2])
        filled = data[3]
        draw_right_triangle(s, filled)
    elif shape == "diamond":
        s = int(data[1])
        filled = data[2]
        draw_diamond(s, filled)