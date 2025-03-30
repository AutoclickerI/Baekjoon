# [Gold II] Ground Defense - 14483 

[문제 링크](https://www.acmicpc.net/problem/14483) 

### 성능 요약

메모리: 356296 KB, 시간: 1156 ms

### 분류

브루트포스 알고리즘, 자료 구조, 느리게 갱신되는 세그먼트 트리, 세그먼트 트리

### 제출 일자

2025년 3월 31일 00:22:21

### 문제 설명

<p>You are a denizen of Linetopia, whose n major cities happen to be equally spaced along an east-west line. In fact, they are often numbered in order from 1 to n, where 1 is the westmost city and n is the eastmost city. Linetopia was a lovely place to live until forces from neighboring Trapez invaded. As part of Linetopia’s Shielding Lives and Protecting Citizens initiative, you have been called upon to process information about Trapezoid troop movements so we can determine which cities have been hardest hit and know where to send reinforcements.</p>

<p>Linetopia intelligence has discovered that the Trapezoid forces are attacking in the following pattern. They are sending massive aircraft to drop troops on Linetopia cities. Each aircraft starts at some city i, dropping s soldiers. The aircraft then proceeds to fly either east or west. Each time it flies over another city, it drops a more soldiers than it dropped on the previous city it passed. After performing d drops, the aircraft returns to Trapez to resupply.</p>

<p>You will be receiving intel updates that inform you of the specs of each Trapezoid aircraft passing over Linetopia. You want to answer queries that ask how many Trapezoid troops have been dropped on a particular city. Are you up to the task?</p>

### 입력 

 <p>The first line of input contains a single integer T (1 ≤ T ≤ 10), the number of test cases. The first line of each test case contains two integers: m (1 ≤ m ≤ 10,000), the number of updates and queries and n (1 ≤ n ≤ 500,000), the number of cities in Linetopia.</p>

<p>The next m lines of input are either updates or queries. Update lines begin with a capital U, then contain either a capital E (east) or W (west) to indicate direction, and then contain four integers i (1 ≤ i ≤ n), s (1 ≤ s ≤ 10,000), a (0 ≤ a ≤ 10,000), and d (1 ≤ d ≤ n). These integers signify the starting city, the starting number of soldiers, the increase in soldiers per city, and the number of drops, respectively. You can assume d never results in an aircraft flying to the west of city 1 or to the east of city n.</p>

<p>Query lines begin with a capital Q, and then contain a single integer i (1 ≤ i ≤ n) indicating the city being queried.</p>

### 출력 

 <p>For each query in the input, output a single line containing the number of Trapezoid troops dropped in that city.</p>

