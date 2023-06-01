# [Gold IV] The Earth is Flat! - 4928 

[문제 링크](https://www.acmicpc.net/problem/4928) 

### 성능 요약

메모리: 30840 KB, 시간: 76 ms

### 분류

자료 구조, 스택, 문자열

### 문제 설명

<p>Consider the following language:</p>

<p>\( expression = \begin{cases} c & \text {where c is a single, lower-case letter} \\ (e_1 e_2 \cdots e_t n) & \text{zero or more expressions followed by a natural number} \end{cases} \)</p>

<p>The left column of the table below includes sample expressions of this language. Now the flattening of an expression is defined as follows: A single letter is flattened to itself. An expression of the form ( e1 e2 ··· et n ) is flattened by concatenating n copies of the concatenation of the flattening of ei. In other words, if f(e) is the flattening of e, and + symbolizes concatenation, then f( (e1 e2 ··· et n) ) is:</p>

<p>\( \underbrace {f(e_1)+f(e_2) +\cdots+f(e_t)}_{once}+\overbrace {f(e_1)+f(e_2)+\cdots+f(e_t)}^{twice}+\cdots+\underbrace {f(e_1)+f(e_2)+\cdots+f(e_t)}_{n^{th} time} \)</p>

<p>The following tables show some sample expressions and the result of flattening each.</p>

<table border="1" cellpadding="1" cellspacing="1" style="width:300px">
	<tbody>
		<tr>
			<td style="text-align:center">expression</td>
			<td style="text-align:center">flattend expression</td>
		</tr>
		<tr>
			<td style="text-align:center">w<br>
			(c 4)<br>
			(a (b c 2) 3)</td>
			<td style="text-align:center">w<br>
			cccc<br>
			abcbcabcbcabcbc</td>
		</tr>
	</tbody>
</table>

<p>Write a program to flatten a given expression.</p>

### 입력 

 <p>Your program will be tested on one or more test cases. Each test case is made of one correctly formed expression written on a separate line. A ’\$’ character identifies the end of line. The last line of the input, which is not part of the test cases, contains a ’\$’ by itself (possibly with leading and/or trailing white spaces). Every expression in the input is grammatically correct according to the grammar specified above. Note that an expression may contain leading, trailing, and/or embedded spaces. Such spaces should be ignored. Letters and numbers are separated from each other by at least one space character.</p>

### 출력 

 <p>For each test case expression, write its flattening on a separate line. There should be no spaces (other than newlines) in the output.</p>

