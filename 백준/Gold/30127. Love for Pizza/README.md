# [Gold I] Love for Pizza - 30127 

[문제 링크](https://www.acmicpc.net/problem/30127) 

### 성능 요약

메모리: 140112 KB, 시간: 468 ms

### 분류

다이나믹 프로그래밍, 자료 구조, 정렬, 기하학, 누적 합, 각도 정렬, 최대 부분 배열 문제

### 제출 일자

2026년 3월 6일 07:14:16

### 문제 설명

<p>My brother and I love pizza. My brother ordered a pizza today with a number of toppings. Some of those toppings I love, like mushrooms, while there are some others that I hate, like olives. Even among the toppings I like (or the ones that I don't like), I like some more than the other, depending on the amount.</p>

<p>Now my brother will let me take a wedge of any size from the pizza. This means I am allowed to make two cuts from the center of the pizza to its circumference, and can keep one of the two resulting pieces. If either cut goes through a topping, the entire topping belongs to that piece which contains the centre of the topping. I am not allowed to cut exactly through the centre of a topping. Each topping will thus remain entirely on one of the pieces. I would like to cut and choose the best piece possible for myself.</p>

### 입력 

 <p>Input contains multiple test-cases. The first line of the input contains <b>T</b>, the number of test cases, followed by <b>T</b> testcases. The first line of each test case contains one integer <b>N</b>, the number of toppings. It is followed by <b>N</b> lines containing three space-separated integers each. Each line described a single topping. The first integer denotes my <b>preference</b> for the topping. The next two integers denote respectively the <b>x</b> and <b>y</b> co-ordinates of the centre of the topping.</p>

### 출력 

 <p>Output a single line per test-case, indicating the sum of the preferences of all the toppings on the best piece. The best piece is the one that has the maximum sum possible.</p>

