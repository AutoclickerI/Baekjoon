# [Bronze I] Alarm Clock - 10372 

[문제 링크](https://acmicpc.net/problem/10372) 

### 선택한 제출

[제출 95190184](https://acmicpc.net/source/95190184) · PyPy3 · 153 B · Alarm Clock.py

### 성능 요약

메모리: 109544 KB, 시간: 92 ms

### 분류

구현, 브루트포스 알고리즘

### 제출 일자

2025년 6월 9일 11:08:44

### 문제 설명

<p>Alice likes her digital alarm clock. She sets them up every evening. Last night Alice had a dream about her clock. Unfortunately, the only thing she is able to remember is the number of highlighted segments of the clock. Alice wonders what time was set on the clock in her dream.</p>

<p>Alice’s clock have four digits: two for hours and two for minutes. For example, the clock below shows 9:30 (note the leading zero).</p>

<p style="text-align:center"><img alt="" src="/upload/images2/alarm1.png" style="height:69px; width:149px"></p>

<p>The clock uses following digit representation.</p>

<p style="text-align:center"><img alt="" src="/upload/images2/alarm2.png" style="height:69px; width:395px"></p>

### 입력 

 <p>The only line of the input file contains single integer n — the number of highlighted segments of the clock in Alice’s dream (0 ≤ n ≤ 30).</p>

### 출력 

 <p>Output five characters in “hh:mm” format — the time shown on the clock in Alice’s dream. The time must be correct: 0 ≤ hh &lt; 24 and 0 ≤ mm &lt; 60. If there are many possible correct times, output any of them. If there is none, output “Impossible”.</p>

