# [Bronze II] Time of the Magical Number - 35005 

[문제 링크](https://www.acmicpc.net/problem/35005) 

### 성능 요약

메모리: 32412 KB, 시간: 52 ms

### 분류

구현, 브루트포스 알고리즘

### 제출 일자

2025년 12월 25일 12:40:58

### 문제 설명

<p>Long ago, in the fairy kingdom of Time, there lived a kind wizard named Nikolay. He adored the magical number 239, which brought him luck and joy every time he saw it on the magical digital clock of the kingdom located at the main square.</p>

<p>This wonderful clock displayed time using four digits: two for the hours and two for the minutes. If the number of hours or minutes was less than $10$, a $0$ was placed in the front.</p>

<p>Nikolay can enchant time so that there will be $H$ hours in each day, numbered from $0$ to $H - 1$, and $M$ minutes in each hour, numbered from $0$ to $M - 1$. For this spell, Nikolay can select any numbers $H$ and $M$ between $10$ and $100$, inclusive.</p>

<p>The time shown by the clock is <em>lucky</em> only when the digits resemble the cherished combination 239:</p>

<ul>
<li>When the clock shows <code>X2:39</code>, where the first digit <code>X</code> can take any value from <code>0</code> to <code>9</code>.</li>
<li>Or <code>2X:39</code>, where the digit <code>X</code> can take the value <code>0</code>, <code>2</code>, or <code>3</code> (because <code>0</code> does not hinder the perception of the magical number).</li>
<li>Or <code>23:X9</code>, where the digit <code>X</code> can take the value <code>0</code>, <code>3</code>, or <code>9</code>.</li>
<li>Or even <code>23:9X</code>, where the digit <code>X</code> can take any value from <code>0</code> to <code>9</code>.</li>
</ul>

<p>One day, Nikolay faced the question: "Given $H$ and $M$, how many minutes in a full day will the clock show a lucky number?" Help Nikolay find this number.</p>

### 입력 

 <p>The first line of input contains two integers $H$ and $M$ separated by a space: the number of hours in a day and the number of minutes in an hour ($10 \le H, M \le 100$).</p>

### 출력 

 <p>Output the number of minutes in a full day when the clock will show a lucky number.</p>

