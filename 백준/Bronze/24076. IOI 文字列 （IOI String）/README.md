# [Bronze II] IOI 文字列 (IOI String) - 24076 

[문제 링크](https://acmicpc.net/problem/24076) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

구현, 문자열

### 제출 일자

2024년 5월 6일 01:48:20

### 문제 설명

<p>長さが奇数&nbsp;<var>N</var>&nbsp;の文字列&nbsp;<var>S</var>&nbsp;が与えられる．<var>S</var>&nbsp;の各文字は英大文字である．</p>

<p><strong>IOI 文字列</strong>とは次の条件をすべて満たす文字列である．</p>

<ul>
	<li>長さが奇数である．</li>
	<li>各文字は&nbsp;<code>I</code>&nbsp;または&nbsp;<code>O</code>&nbsp;で，これらが交互に連なる．</li>
	<li><var>1</var>&nbsp;文字目は&nbsp;<code>I</code>&nbsp;である．</li>
</ul>

<p>例えば，<code>I</code>，<code>IOI</code>，<code>IOIOIOI</code>&nbsp;は IOI 文字列であるが，<code>JOI</code>，<code>IIOOII</code>，<code>OIOIO</code>&nbsp;は IOI 文字列ではない．</p>

<p>あなたは次の操作を&nbsp;<var>0</var>&nbsp;回以上繰り返すことができる．</p>

<ul>
	<li>文字列&nbsp;<var>S</var>&nbsp;の文字を&nbsp;<var>1</var>&nbsp;つ選び，好きな英大文字に変更する．</li>
</ul>

<p>文字列&nbsp;<var>S</var>&nbsp;を IOI 文字列にするのに必要な操作の回数の最小値を求めよ．</p>

### 입력 

 <p>入力は以下の形式で標準入力から与えられる．</p>

<pre><var>N</var>
<var>S</var></pre>

### 출력 

 <p>文字列&nbsp;<var>S</var>&nbsp;を IOI 文字列にするのに必要な操作の回数の最小値を出力せよ．</p>

