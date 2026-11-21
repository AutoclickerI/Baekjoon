# [Silver V] Dungeon Equilibrium - 35230 

[문제 링크](https://acmicpc.net/problem/35230) 

### 성능 요약

메모리: 32412 KB, 시간: 28 ms

### 분류

구현

### 제출 일자

2026년 2월 11일 12:36:34

### 문제 설명

<p>You are developing a new RPG game where each monster species has a peculiar rule about how many times it should appear on a level.</p>

<p>A level is represented by an array of integers $a_1, a_2, \dots , a_n$, where each integer represents the type of a monster.</p>

<p>A level is considered balanced if, for every monster type $x$ that appears, there are exactly $x$ monsters of that type. For example, a balanced level might have three monsters of type $3$, five of type $5$, and so on. An empty level (no monsters at all) is also considered balanced.</p>

<p>Unfortunately, your current level design is not necessarily balanced. You can delete some monsters (i.e., remove elements from the array) to make it balanced.</p>

<p>Given the array $a_1, a_2, \dots , a_n$, find the minimum number of monsters you need to remove to make the level balanced.</p>

### 입력 

 <p>The first line contains an integer $n$ ($1 ≤ n ≤ 1000$) — the current number of monsters in the level.</p>

<p>The second line contains $n$ integers $a_1, a_2, \dots , a_n$ ($0 ≤ a_i ≤ n$) — the monster types.</p>

### 출력 

 <p>Output a single line containing an integer: the minimum number of monsters you should remove from the level to make it balanced.</p>

