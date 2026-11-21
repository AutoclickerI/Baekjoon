# [Unrated] 갓 소수 - 17118 

[문제 링크](https://acmicpc.net/problem/17118) 

### 성능 요약

메모리: 32400 KB, 시간: 92 ms

### 분류

수학, 정수론, 페르마의 소정리

### 제출 일자

2022년 8월 3일 09:49:03

### 문제 설명

<p>키파는 소수를 좋아한다. 키파가 제일 좋아하는 소수를 <em>p</em>라 하자. <em>a</em> = 860798509, <em>b</em> = 198609463, <em>N</em> = <em>p</em>, <i>x</i><sub>0</sub> = <em>n</em>으로 LCG를 돌려서 <em>x<sub>p</sub></em>의 값을 출력하라.</p>

<p>LCG(Linear Congruential Generator)의 정의는 다음과 같은 수열 {<em>x<sub>i</sub></em>}이다: 모든 자연수 <em>k</em>에 대해,</p>

<p style="text-align: center;"><em>x<sub>k</sub></em> = <em>ax<sub>k</sub></em><sub>-1</sub> + <em>b</em> (mod <em>N</em>), 0 ≤ <em>x<sub>k</sub></em> &lt; <em>N</em>.</p>

<p>LCG는 다양한 곳에서 사용되는데, 예를 들어 C의 <code>rand()</code>, Java의 <code>Random.nextInt()</code>, 그리고 제1회 구데기컵의 <a href="https://www.acmicpc.net/problem/15636" target="_blank">이 문제</a>가 있다.</p>

### 입력 

 <p><i>n</i>이 주어진다.&nbsp;<code>int</code> 범위임이 보장된다.</p>

### 출력 

 <p>문제에 해당하는 답을 출력한다.</p>

