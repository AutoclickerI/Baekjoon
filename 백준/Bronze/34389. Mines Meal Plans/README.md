# [Bronze II] Mines Meal Plans - 34389 

[문제 링크](https://www.acmicpc.net/problem/34389) 

### 성능 요약

메모리: 32412 KB, 시간: 36 ms

### 분류

수학, 구현, 사칙연산

### 제출 일자

2025년 9월 25일 08:26:04

### 문제 설명

<p>Students at Mines who live in the residence halls must have a meal plan. The following meal plans are available:</p>

<table class="table table-bordered">
	<tbody>
		<tr>
			<th>Plan</th>
			<th>Info</th>
		</tr>
		<tr>
			<td>Marble</td>
			<td>$19$ meals/week, $\$200$ Munch Money</td>
		</tr>
		<tr>
			<td>Marble+</td>
			<td>$19$ meals/week, $\$350$ Munch Money</td>
		</tr>
		<tr>
			<td>Quartz</td>
			<td>$14$ meals/week, $\$200$ Munch Money</td>
		</tr>
		<tr>
			<td>Quartz+</td>
			<td>$14$ meals/week, $\$350$ Munch Money</td>
		</tr>
	</tbody>
</table>

<p>A student can get a meal by either using one of their meals swipes, or spending some of their Munch Money. If they have used all of their meal swipes or spent all of their munch money for their meal plan, then they can no longer use that option to get a meal. Given data about the meal swipes and Munch Money used by a student, can you determine what options they have for getting a meal?</p>

### 입력 

 <p>The first line of input will be an integer $1 \leq N \leq 100$, the number of students to follow. The next $N$ lines will have four space-separated values: a string containing the name of the student, a string containing the name of their meal plan, an integer representing how many meal swipes they have used, and a real number with at most $2$ digits after the decimal point representing how much munch money they have left.</p>

<p>Input Restrictions</p>

<ul>
	<li>The meal plan names will be one of "Marble", "Marble+", "Quartz", or "Quartz+".</li>
	<li>Munch Money spent will be between $0.00$ and the maximum amount of munch money allowed by the meal plan.</li>
	<li>The number of meal swipes used will be between $0$ and the maximum amount of meal swipes allowed by the plan.</li>
</ul>

<p>Money values are guaranteed to be given with at least one digit before the decimal point, and exactly two digits after the decimal point. The whole-number part of the value will not have any unnecessary leading zeros.</p>

### 출력 

 <p>Output should be in the format <code>X Y Z Custom Text</code> where <code>X</code> is the student's name, <code>Y</code> is the student's remaining number of meal swipes, and <code>Z</code> is the student's remaining amount of munch money, and <code>Custom Text</code> is one of the following depending on which of the four scenarios have occurred:</p>

<ul>
	<li><code>Use meal swipe or munch money</code> --- the student has meal swipes left and munch money left,</li>
	<li><code>Use munch money</code> --- the student has no meal swipes left, but has munch money,</li>
	<li><code>Use meal swipe</code> --- the student has no munch money left, but has meal swipes remaining,</li>
	<li><code>Go to Downtown Golden!</code> --- the student has no munch money and no meal swipes remaining.</li>
</ul>

<p>Munch money should be printed with at least one digit before the decimal point, and exactly two digits after the decimal point. The whole-number part of the value must not have any unnecessary leading zeros.</p>

