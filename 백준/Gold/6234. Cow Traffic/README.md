# [Gold III] Cow Traffic - 6234 

[문제 링크](https://www.acmicpc.net/problem/6234) 

### 성능 요약

메모리: 37164 KB, 시간: 372 ms

### 분류

그래프 이론, 위상 정렬, 방향 비순환 그래프

### 제출 일자

2025년 4월 1일 22:49:37

### 문제 설명

<p>The bovine population boom down on the farm has caused serious congestion on the cow trails leading to the barn. Farmer John has decided to conduct a study to find the bottlenecks in order to relieve the 'traffic jams' at milking time.</p>

<p>The pasture contains a network of <i>M</i> (1 ≤ <i>M</i> ≤ 50,000) one-way trails, each of which connects exactly two different intersections from the set of <i>N</i> (1 ≤ <i>N</i> ≤ 5,000) intersections conveniently numbered 1..<i>N</i>; the barn is at intersection number <i>N</i>. Each trail connects one intersection point to another intersection point with a higher number. As a result, there are no cycles and, as they say on the farm, all trails lead to the barn. A pair of intersection points might be connected by more than one trail.</p>

<p>During milking time rush hour, the cows start from their respective grazing locations and head to the barn. The grazing locations are exactly those intersection points with no trails connecting into them. Each cow traverses a 'path', which is defined as a sequence of trails from a grazing location to the barn.</p>

<p>Help FJ finding the busiest trail(s) by computing the largest number of possible paths that contain any one trail. The answer is guaranteed to fit in a signed 32-bit integer.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: <i>N</i> and <i>M</i>.</li>
	<li>Lines 2..<i>M</i>+1: Two space-separated intersection points.</li>
</ul>

### 출력 

 <ul>
	<li>Line 1: The maximum number of paths passing through any one trail.</li>
</ul>

