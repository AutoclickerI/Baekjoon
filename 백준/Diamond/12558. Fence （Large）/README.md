# [Diamond V] Fence (Large) - 12558 

[문제 링크](https://acmicpc.net/problem/12558) 

### 성능 요약

메모리: 211828 KB, 시간: 7716 ms

### 분류

수학, 그래프 이론, 그리디 알고리즘, 정수론, 최단 경로, 데이크스트라, 0-1 너비 우선 탐색

### 제출 일자

2026년 3월 29일 13:06:12

### 문제 설명

<p>We are looking into building a very long fence. We have already found a nice place to build it, and all that remains is to collect the materials.</p>

<p>From local hardware stores, we can buy unlimited numbers of wooden boards, each of which can come in a variety of different lengths. To avoid waste, we want to make sure that the total length of these boards is&nbsp;<em>exactly</em>&nbsp;equal to the length of the fence we are trying to build.</p>

<p>Given the length of the fence, and the possible board lengths that we can use, what is the minimum number of boards that we need to purchase in order to get exactly the right length?</p>

<p><em>Beware:</em>&nbsp;the fence is going to be very long!</p>

### 입력 

 <p>The first line of the input file contains the number of cases,&nbsp;<strong>T</strong>.&nbsp;<strong>T</strong>&nbsp;test cases follow.</p>

<p>Each test case consists of two lines. The first line contains space-separated integers&nbsp;<strong>L</strong>and&nbsp;<strong>N</strong>. These represent the total length of the fence, and the number of different board lengths that can be purchased. The second line contains&nbsp;<strong>N</strong>&nbsp;space-separated integers&nbsp;<strong>B<sub>1</sub></strong>,&nbsp;<strong>B<sub>2</sub></strong>, ...,&nbsp;<strong>B<sub>N</sub></strong>, representing all the possible board lengths.</p>

<h3>Limits</h3>

<ul>
	<li>1 ≤&nbsp;<strong>T</strong>&nbsp;≤ 50.</li>
	<li>10<sup>10</sup>&nbsp;≤&nbsp;<strong>L</strong>&nbsp;≤ 10<sup>18</sup>.</li>
	<li>1 ≤&nbsp;<strong>N</strong>&nbsp;≤ 100.</li>
	<li><span style="font-size:13px">1 ≤&nbsp;</span><strong>B<sub>i</sub></strong><span style="font-size:13px">&nbsp;≤ 100000.</span></li>
</ul>

### 출력 

 <p>For each test case, output one line containing "Case #x: M", where x is the case number (starting from 1) and M is as follows:</p>

<ul>
	<li>If it is possible to purchase one or more boards so that their total length is exactly equal to&nbsp;<strong>L</strong>, then M should be the minimum number of boards required to do this.</li>
	<li>Otherwise, M should be the string "IMPOSSIBLE".</li>
</ul>

