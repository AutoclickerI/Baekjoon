# [Diamond IV] Subsets - 8382 

[문제 링크](https://www.acmicpc.net/problem/8382) 

### 성능 요약

메모리: 136748 KB, 시간: 1240 ms

### 분류

수학, 분할 정복을 이용한 거듭제곱, 고속 푸리에 변환, 생성 함수

### 제출 일자

2026년 2월 17일 14:21:20

### 문제 설명

<p>We are going to consider subsets <em>P</em> of a given set {1, ..., <em>n</em>}. We are interested in subsets such that for a given natural number <em>x</em> > 1 and for any natural number <em>y</em> at least one of the numbers <em>y</em>, <em>x</em> · <em>y</em> doesn't belong to <em>P</em>. We would like to calculate the number of such subsets, that have exactly <em>k</em> elements. It is possible that the number of such subsets is huge - therefore it is sufficient to calculate the remainder of the division of the result by <em>m</em>.</p>

<p>Write a program which:</p>

<ul>
	<li>reads from the standard input four integers: <em>n</em>, <em>m</em>, <em>k</em> and <em>x</em>,</li>
	<li>calculates the remainder of the division by <em>m</em> of the number of <em>k</em>-element subsets of set {1, ..., <em>n</em>}, that fulfill the requirements described above,</li>
	<li>writes result to the standard output.</li>
</ul>

### 입력 

 <p>In the first and only line of the standard input there are four integers <em>n</em>, <em>m</em>, <em>k</em> and <em>x</em> (1 ≤ <em>n</em> ≤ 10<sup>18</sup>, 2 ≤ <em>m</em> ≤ 1 000 000, 0 ≤ <em>k</em> ≤ 1 000, 2 ≤ <em>x</em> ≤ 10), separated by single spaces.</p>

### 출력 

 <p>The first and only line should contain one integer - the reminder of the division by <em>m</em> of the number of <em>k</em>-element subsets of set {1, ..., <em>n</em>} that fulfill the specified requirements.</p>

