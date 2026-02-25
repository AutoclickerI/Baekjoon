# [Bronze I] Shinjuku Station - 35369 

[문제 링크](https://www.acmicpc.net/problem/35369) 

### 성능 요약

메모리: 32412 KB, 시간: 48 ms

### 분류

수학, 구현, 문자열, 브루트포스 알고리즘, 사칙연산

### 제출 일자

2026년 2월 25일 11:47:14

### 문제 설명

<p>Audrey is planning her first day of vacation in Tokyo! Her first stop is a Honkai: Star Rail pop-up shop. She has heard from her friends that the trains in Japan are a lot like her favorite train, the Astral Express, so she decides to take a series of trains to the pop-up. As luck would have it, she has to transfer at Shinjuku Station, the largest train station in Tokyo.</p>

<p>Audrey is thinking of taking one of the $n$ trains that will arrive at Shinjuku Station, and then transferring to one of the $m$ trains that will depart from Shinjuku Station. The trains in Tokyo are extremely reliable, and Audrey knows to the second when each train will arrive at or depart from Shinjuku Station.</p>

<p>Audrey is a bit nervous about transferring at Shinjuku Station, so she does not want to have a tight transfer that takes <i>strictly</i> fewer than $s$ seconds. However, neither does Audrey want to spend too long transferring at Shinjuku Station. Help Audrey determine the minimum transfer time possible. Audrey will not consider any itineraries that cross the boundary of a calendar day.</p>

### 입력 

 <p>The first line of input contains two integers $n$ and $m$ ($1 \le n, m \le 50$), the number of trains entering and leaving Shinjuku Station, respectively.</p>

<p>The next $n$ lines each contain a string of the form <code>HH:MM:SS</code>, indicating the exact arrival time of a train entering Shinjuku.</p>

<p>The next $m$ lines each contain a string of the form <code>HH:MM:SS</code>, indicating the exact departure time of a train leaving Shinjuku.</p>

<p>It is guaranteed that each of these times is a valid time. Specifically, <code>HH</code> is an integer between $5$ and $23$ inclusive, and both <code>MM</code> and <code>SS</code> are non-negative integers between $0$ and $59$. All values are represented using two digits, possibly with a leading zero.</p>

<p>The last line contains a single integer $s$ ($1 \le s \le 600$), representing the minimum transfer time in seconds required by Audrey.</p>

### 출력 

 <p>Output a single integer, the minimum number of seconds that Audrey needs for a valid transfer. If no such transfer exists, output $-1$.</p>

