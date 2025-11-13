# [Unrated] HQ0-9+-INCOMPUTABLE?! - 23363 

[문제 링크](https://www.acmicpc.net/problem/23363) 

### 성능 요약

메모리: 4528 KB, 시간: 0 ms

### 분류

런타임 전의 전처리, 해 구성하기, 정수론, 수학

### 제출 일자

2025년 11월 14일 07:42:33

### 문제 설명

<p>HQ9+ is an esoteric programming language specialized for certain tasks. For example, printing “Hello, world!” or writing a quine (a program that prints itself) couldn’t be any simpler. Unfortunately, HQ9+ doesn’t do very well in most other situations. This is why we have created our own variant of the language, HQ0-9+-INCOMPUTABLE?!.</p>

<p>A HQ0-9+-INCOMPUTABLE?! program is a sequence of commands, written on one line without any whitespace (except for the trailing newline). The program can store data in two memory areas: the buffer, a string of characters, and the accumulator, an integer variable. Initially, the buffer is empty and the accumulator is set to 0. The value of the buffer after executing all the commands becomes the program’s output.</p>

<p>HQ0-9+-INCOMPUTABLE?! supports the following commands:</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<th>command</th>
			<th>description</th>
		</tr>
		<tr>
			<td><code>h</code>, <code>H</code></td>
			<td>appends <code>helloworld</code> to the buffer</td>
		</tr>
		<tr>
			<td><code>q</code>, <code>Q</code></td>
			<td>appends the program source code to the buffer (not including the trailing newline)</td>
		</tr>
		<tr>
			<td><code>0-9</code></td>
			<td>replaces the buffer with n copies of its old value – for example, ‘<code>2</code>’ doubles the buffer</td>
		</tr>
		<tr>
			<td><code>+</code></td>
			<td>increments the accumulator</td>
		</tr>
		<tr>
			<td><code>-</code></td>
			<td>decrements the accumulator</td>
		</tr>
		<tr>
			<td><code>i</code>, <code>I</code></td>
			<td>increments the ASCII value of every character in the buffer</td>
		</tr>
		<tr>
			<td><code>n</code>, <code>N</code></td>
			<td>applies ROT13 to the letters and numbers in the buffer (for letters ROT13 preserves case; for digits we define ROT13(d) = (d + 13) mod 10)</td>
		</tr>
		<tr>
			<td><code>c</code>, <code>C</code></td>
			<td>swaps the case of every letter in the buffer; doesn’t change other characters</td>
		</tr>
		<tr>
			<td><code>o</code>, <code>O</code></td>
			<td>removes all characters from the buffer such that their index, counted from the end, is a prime or a power of two (or both); the last character has index 1 (which is a power of 2)</td>
		</tr>
		<tr>
			<td><code>m</code>, <code>M</code></td>
			<td>sets the accumulator to the current buffer length</td>
		</tr>
		<tr>
			<td><code>p</code>, <code>P</code></td>
			<td>removes all characters from the buffer such that their index is a prime or a power of two (or both); the first character has index 1 (which is a power of 2)</td>
		</tr>
		<tr>
			<td><code>u</code>, <code>U</code></td>
			<td>converts the buffer to uppercase</td>
		</tr>
		<tr>
			<td><code>t</code>, <code>T</code></td>
			<td>sorts the characters in the buffer by their ASCII values</td>
		</tr>
		<tr>
			<td><code>a</code>, <code>A</code></td>
			<td>replaces every character in the buffer with its ASCII value in decimal (1–3 digits)</td>
		</tr>
		<tr>
			<td><code>b</code>, <code>B</code></td>
			<td>replaces every character in the buffer with its ASCII value in binary (exactly eight ‘0’/‘1’ characters)</td>
		</tr>
		<tr>
			<td><code>l</code>, <code>L</code></td>
			<td>converts the buffer to lowercase</td>
		</tr>
		<tr>
			<td><code>e</code>, <code>E</code></td>
			<td>translates every character in the buffer to l33t using the following table:
			<pre>ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz 0123456789
48(03=6#|JXLM 09Q257UVW%Y2 a6<d3f9hijk1m^0p9r57uvw*y2 O!ZEA$G/B9</pre>
			</td>
		</tr>
		<tr>
			<td><code>?</code></td>
			<td>removes 47 characters from the end of the buffer (or everything if it is too short)</td>
		</tr>
		<tr>
			<td><code>!</code></td>
			<td>removes 47 characters from the beginning of the buffer (or everything if it is too short)</td>
		</tr>
	</tbody>
</table>

<p>As you can see, HQ0-9+-INCOMPUTABLE?! is much more powerful than HQ9+. Demonstrate this by writing and submitting a HQ0-9+-INCOMPUTABLE?! program that outputs <span class="TIS">10812199111114105115</span>.</p>

### 입력 

 Empty

### 출력 

 Empty

