# [Bronze II] 巻物 (Scroll) - 22016 

[문제 링크](https://acmicpc.net/problem/22016) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

구현, 문자열

### 제출 일자

2024년 5월 8일 18:28:50

### 문제 설명

<p>JOI 高校の生徒である葵は，図書室で巻物を見つけた．この巻物には長さ&nbsp;<var>N</var>&nbsp;の文字列&nbsp;<var>S</var>&nbsp;が書かれており，文字列&nbsp;<var>S</var>&nbsp;の各文字は&nbsp;<code>j</code>，<code>o</code>，<code>i</code>，<code>J</code>，<code>O</code>，<code>I</code>&nbsp;のいずれかである．</p>

<p>この巻物は持ち出しが禁じられているため，葵は文字列&nbsp;<var>S</var>&nbsp;をすべて書き写すことにした．葵が記した文字列は&nbsp;<var>T</var>&nbsp;である．</p>

<p>しかし，葵は誤って前から&nbsp;<var>K</var>&nbsp;番目 (<var>1 ≦ K ≦ N</var>) 以降の文字（<var>K</var>&nbsp;番目の文字を含む）の大文字と小文字を逆に記してしまった．すなわち，<var>1 ≦ i ≦ K-1</var>&nbsp;のとき，<var>S</var>&nbsp;の&nbsp;<var>i</var>&nbsp;番目の文字と&nbsp;<var>T</var>&nbsp;の&nbsp;<var>i</var>&nbsp;番目の文字は等しく，<var>K ≦ i ≦ N</var>&nbsp;のとき，<var>S</var>&nbsp;の&nbsp;<var>i</var>&nbsp;番目の文字が大文字であれば&nbsp;<var>T</var>&nbsp;の&nbsp;<var>i</var>&nbsp;番目の文字は小文字であり，<var>S</var>&nbsp;の&nbsp;<var>i</var>&nbsp;番目の文字が小文字であれば&nbsp;<var>T</var>&nbsp;の&nbsp;<var>i</var>&nbsp;番目の文字は大文字である．</p>

<p>文字列&nbsp;<var>T</var>&nbsp;とその長さ&nbsp;<var>N</var>，値&nbsp;<var>K</var>&nbsp;が与えられたとき，巻物に書かれていた文字列&nbsp;<var>S</var>&nbsp;を復元するプログラムを作成せよ．</p>

### 입력 

 <p>入力は以下の形式で標準入力から与えられる．</p>

<pre><var>N</var> <var>K</var>
<var>T</var></pre>

### 출력 

 <p>標準出力に，巻物に書かれていた文字列&nbsp;<var>S</var>&nbsp;を&nbsp;<var>1</var>&nbsp;行で出力せよ．</p>

