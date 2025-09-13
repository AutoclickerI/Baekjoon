# [Silver V] Club Pizza - 34291 

[문제 링크](https://www.acmicpc.net/problem/34291) 

### 성능 요약

메모리: 33432 KB, 시간: 36 ms

### 분류

그리디 알고리즘, 정렬

### 제출 일자

2025년 9월 13일 11:36:03

### 문제 설명

<p>When Blaster first started at Mines, he joined as many different extracurricular clubs as he could. He loves getting involved on campus, and he also loves that many clubs provide free pizza! Unfortunately, now he is in too many clubs, and some of the meetings overlap. Additionally, if he eats too much pizza, then he will be too full to do any more activities.</p>

<p>Blaster still wants to attend as many clubs as he can. Each club meeting is only one hour long, but some club meetings might be at the same time as each other. Different clubs give different amounts of pizza, so he needs to decide which meetings to go to in order to maximize the amount of clubs he goes to before getting full of pizza.</p>

<p>If Blaster chooses optimally, how many clubs will he be able to attend?</p>

### 입력 

 <p>The first line of the input consists of two integers $n,c$ ($1 \leq n \leq 10^3, 0 \leq c \leq 10^6$)---the number of clubs and the number of pizza slices Blaster can eat before being full, respectively.</p>

<p>The $i$-th line of the following $n$ lines contains two integers $t_i, p_i$ ($0 \leq t_i < 24, 0 \leq p_i \leq 10^6$)---the hour of the day that the $i$-th club meets at and the number of pizza slices he will eat at the $i$-th meeting, respectively.</p>

### 출력 

 <p>Output a single integer, the number of clubs that Blaster can attend.</p>

