# [Bronze III] Hotelier - 27481 

[문제 링크](https://acmicpc.net/problem/27481) 

### 성능 요약

메모리: 31256 KB, 시간: 76 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2023년 2월 17일 16:00:52

### 문제 설명

<p>Amugae has a hotel consisting of $10$ rooms. The rooms are numbered from $0$ to $9$ from left to right.</p>

<p>The hotel has two entrances --- one from the left end, and another from the right end. When a customer arrives to the hotel through the left entrance, they are assigned to an empty room closest to the left entrance. Similarly, when a customer arrives at the hotel through the right entrance, they are assigned to an empty room closest to the right entrance.</p>

<p>One day, Amugae lost the room assignment list. Thankfully Amugae’s memory is perfect, and he remembers all of the customers: when a customer arrived, from which entrance, and when they left the hotel. Initially the hotel was empty. Write a program that recovers the room assignment list from Amugae’s memory.</p>

### 입력 

 <p>The first line consists of an integer $n$ ($1\le n\le 10^5$), the number of events in Amugae’s memory.</p>

<p>The second line consists of a string of length $n$ describing the events in chronological order. Each character represents:</p>

<ul>
	<li>‘<code>L</code>’: A customer arrives from the left entrance.</li>
	<li>‘<code>R</code>’: A customer arrives from the right entrance.</li>
	<li>‘<code>0</code>’, ‘<code>1</code>’, …, ‘<code>9</code>’: The customer in room $x$ ($0$, $1$, …, $9$ respectively) leaves.</li>
</ul>

<p>It is guaranteed that there is at least one empty room when a customer arrives, and there is a customer in the room $x$ when $x$ ($0$, $1$, …, $9$) is given. Also, all the rooms are initially empty.</p>

### 출력 

 <p>In the only line, output the hotel room’s assignment status, from room $0$ to room $9$. Represent an empty room as ‘<code>0</code>’, and an occupied room as ‘<code>1</code>’, without spaces.</p>

