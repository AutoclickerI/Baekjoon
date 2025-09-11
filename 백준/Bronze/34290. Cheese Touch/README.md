# [Bronze I] Cheese Touch - 34290 

[문제 링크](https://www.acmicpc.net/problem/34290) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

구현

### 제출 일자

2025년 9월 12일 06:12:24

### 문제 설명

<p>Colorado School of Mines has a big problem! Somebody left a piece of cheese in front of the Student Center, and now several students are infected with the "cheese touch". These infected students can spread it to anyone adjacent to them, but not through walls. Although a cure is being developed, it may not come fast enough to stop the spread.</p>

<p>The "cheese touch" spreads every $p$ minutes (at times $p, 2p, 3p, \ldots$), infecting people directly adjacent to infected individuals. The cure will be ready after $t$ minutes. The cure acts immediately, so the infection is not spread at time $t$ or any time after.</p>

### 입력 

 <p>The first line of input contains two integers $p$ ($1 \leq p \leq 3000$) and $t$ ($1 \leq t \leq 3000$) representing the minutes it takes for the "cheese touch" to spread and the minutes it takes to find a cure, respectively.</p>

<p>The second line contains a single string $s$ ($1 \leq |s| \leq 3000$) consisting of the characters '<code>H</code>', '<code>I</code>', and '<code>W</code>' representing the initial configuration of Healthy people, Infected people, and Walls, respectively. It is guaranteed that there will be at least $1$ healthy person.</p>

### 출력 

 <p>Print out "<code>CURED</code>" if the cure was released before all the healthy people became infected or "<code>ALL INFECTED</code>" if the cure came too late (without quotes).</p>

