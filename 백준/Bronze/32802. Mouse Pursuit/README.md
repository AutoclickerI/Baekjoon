# [Bronze II] Mouse Pursuit - 32802 

[문제 링크](https://www.acmicpc.net/problem/32802) 

### 성능 요약

메모리: 40092 KB, 시간: 180 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2024년 12월 5일 14:22:42

### 문제 설명

<p>Brandon is playing the newest idle game, Mouse Pursuit! The goal of this game is to pursue mice for cheese and glory.</p>

<p>In Mouse Pursuit, an <em>event</em> consists of pursuing a mouse. If the mouse is caught, the player might earn cheese and glory. However, if the mouse is not caught, the player might lose cheese and glory.</p>

<p>Given Brandon's recent events, Brandon wants to know how much cheese and glory he earned in the last $k$ seconds.</p>

### 입력 

 <p>The first line of input contains a single integer, $n$ $(1 \le n \le 10^5)$.</p>

<p>The next $n$ lines take one of two forms:</p>

<ul>
	<li>$\text{CAUGHT}$ $s$ $c$ $g$: A mouse was caught exactly $s$ seconds ago. The player gained $c$  pieces of cheese and $g$ units of glory.</li>
	<li>$\text{MISS}$ $s$ $c$ $g$: A mouse was missed exactly $s$ seconds ago. The player lost $c$  pieces of cheese and $g$ units of glory.</li>
</ul>

<p>For all events, $0 \le c, g \le 10^6$ and $1 \le s \le 10^9$. It is guaranteed that no two events happened at exactly the same time.</p>

<p>The last line contains a single integer $k$. It is guaranteed that no event happened exactly $k$ seconds ago.</p>

### 출력 

 <p>Output two integers - the number of pieces of cheese Brandon gained in the last $k$ seconds, and the number of units of glory Brandon gained in the last $k$ seconds.</p>

