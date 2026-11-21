# [Bronze III] Keystroke - 20268 

[문제 링크](https://www.acmicpc.net/problem/20268) 

### 선택한 제출

[제출 61265418](https://acmicpc.net/source/61265418) · Python 3 · 170 B · Keystroke.py

### 성능 요약

메모리: 31256 KB, 시간: 48 ms

### 분류

구현

### 문제 설명

<p>You are designing a numeric keypad for numbers 1 to 4, where each number is associated with a unique key. All of the keys are arranged as a 2 × 2 matrix, and there is a detection circuit beneath the keypad. When a key is pressed, the circuit will transmit the keystroke signals to the controller, which will receive its row number and column number. We can use a pair (<code>row</code>, <code>column</code>) to represent an event of a keystroke. Precisely speaking, when you press the key of number 𝑖 where 𝑖 ∈ {1, 2, 3, 4}, the controller will receive the pair (⌊(i − 1)/2⌋,(i − 1) mod 2). For example, when you press key 3, the controller gets (1, 0) as the keystroke signal. You would like to press several keys at the same time for some reason. When you do this, the controller can still receive their corresponding row/column numbers. However, their row numbers are mixed together, as well as the column numbers. For example, when you press keys 1 and 4 simultaneously, the controller would get row numbers {0, 1} and column numbers {0, 1}, because key 1 emits (0, 0) and key 4 emits (1, 1). Another example is that when you pressed keys 1 and 2 simultaneously, the controller can only receive ({0}, {0, 1}) because key 1 emits (0, 0) and key 2 emits (0, 1) and their row numbers are the same. Notice that different keystroke combinations may lead to the same signal. Press keys 2 and 3 would get ({0, 1}, {0, 1}) which is identical to press 1 and 4. Press keys 1, 2, 3, 4 simultaneously would get the same result. Given a keystroke signal, which is in the (<code>row</code>, <code>column</code>)-paired form, please write a program to identify the total number of possible keystroke combinations that can lead to this signal.</p>

### 입력 

 <p>The first line of the input is a positive integer that specifies the number of test cases. Each test case follows immediately in the next line after the previous one. In each test case, its first line gives you two positive integers m and n. Its second line gives you m distinct integers that are the received row numbers. Its third line gives you n distinct integers that are the received column numbers. All numbers in the same line are space-delimited.</p>

### 출력 

 <p>Output the result in a single line for each test case.</p>

