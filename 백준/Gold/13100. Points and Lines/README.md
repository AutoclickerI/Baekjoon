# [Gold I] Points and Lines - 13100 

[문제 링크](https://www.acmicpc.net/problem/13100) 

### 성능 요약

메모리: 39612 KB, 시간: 152 ms

### 분류

자료 구조, 해시를 사용한 집합과 맵, 구현, 파싱, 스택, 문자열

### 문제 설명

<p>One day, you found an old scroll with strange texts on it.</p>

<p>You revealed that the text was actually an expression denoting the position of treasure. The expression consists of following three operations:</p>

<ul>
	<li>From two points, yield a line on which the points lie.</li>
	<li>From a point and a line, yield a point that is symmetric to the given point with respect to the line.</li>
	<li>From two lines, yield a point that is the intersection of the lines.</li>
</ul>

<p>The syntax of the expression is denoted by following BNF:</p>

<pre><code><expression>      ::= <point>
<point>           ::= <point-factor> | <line> "@" <line-factor> | <line> "@" <point-factor> | <point> "@" <line-factor>
<point-factor>    ::= "(" <number> "," <number> ")" | "(" <point> ")"
<line>            ::= <line-factor> | <point> "@" <point-factor>
<line-factor>     ::= "(" <line> ")"
<number>          ::= <zero-digit> | <positive-number> | <negative-number>
<positive-number> ::= <nonzero-digit> | <positive-number> <digit>
<negative-number> ::= "-" <positive-number>
<digit>           ::= <zero-digit> | <nonzero-digit>
<zero-digit>      ::= "0"
<nonzero-digit>   ::= "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9"</code></pre>

<p>Each <point> or <point-factor> denotes a point, whereas each <line> or <line-factor> denotes a line. The former notion of <point-factor> (X,Y) represents a point which has X for x-coordinate and Y for y-coordinate on the 2-dimensional plane. "@" indicates the operations on two operands. Since each operation is distinguishable from others by its operands' types (i.e. a point or a line), all of these operations are denoted by the same character "@". Note that "@" is left-associative, as can be seen from the BNF.</p>

<p>Your task is to determine where the treasure is placed.</p>

### 입력 

 <p>The input consists of multiple datasets. Each dataset is a single line which contains an expression denoting the position of treasure.</p>

<p>It is guaranteed that each dataset satisfies the following conditions:</p>

<ul>
	<li>The length of the string never exceeds 10<sup>2</sup>.</li>
	<li>If both operands of "@" are points, their distance is greater than 1.</li>
	<li>If both operands of "@" are lines, they are never parallel.</li>
	<li>The absolute values of points' coordinates never exceed 10<sup>2</sup> at any point of evaluation.</li>
</ul>

<p>You can also assume that there are at most 100 datasets.</p>

<p>The input ends with a line that contains only a single "#".</p>

### 출력 

 <p>For each dataset, print the X and Y coordinates of the point, denoted by the expression, in this order.</p>

<p>The output will be considered correct if its absolute or relative error is at most 10<sup>−2</sup>.</p>

