# [Bronze III] Divar’s Salaries - 33192 

[문제 링크](https://www.acmicpc.net/problem/33192) 

### 성능 요약

메모리: 32412 KB, 시간: 32 ms

### 분류

사칙연산, 구현, 수학

### 제출 일자

2025년 2월 2일 20:08:41

### 문제 설명

<p>Amin works in the financial department of Divar company. As part of his responsibilities, he needs to prepare the salary payment list for the company’s employees. The salary of each employee is calculated based on a base hourly rate of $x$ Rials. However, the actual pay rate varies depending on the type of working hours:</p>

<ul>
	<li><strong>Normal Working Hours</strong>: Paid at the standard rate of $x$ Rials per hour.</li>
	<li><strong>Overtime Hours</strong>: Any hours worked beyond the standard $140$ hours per month are compensated at $1.5$ times the base rate.</li>
	<li><strong>Holiday Hours</strong>: Hours worked on recognized holidays are paid at twice the base rate, regardless of whether they fall within or beyond the standard $140$ hours.</li>
</ul>

<p>Holiday hours always take precedence, and employees are compensated at the doubled rate for these hours, irrespective of the standard working hour limits.</p>

<p>Amin’s task is to calculate the total monthly salary for each employee, taking into account their normal hours, overtime hours, and holiday hours. Help Amin determine the payment for all the employees in the company.</p>

### 입력 

 <p>The first line of input contains a single integer $n$ ($1 \le n \le 1\, 000$), representing the number of employees in the company. The following $n$ lines each provide three integers $x$, $k$ and $h$, which describe the details for each employee:</p>

<ul>
	<li>$x$ ($100 \le x \le 10^6$): The hourly wage in Rials, which is always a multiple of $10$.</li>
	<li>$k$ ($0 \le k \le 480$): The total number of hours worked during the current month.</li>
	<li>$h$ ($0 \le h \le k$): The number of holiday hours worked.</li>
</ul>

### 출력 

 <p>In the output, print the total monthly payment for each employee on a separate line. The payment must be formatted with commas separating every three digits, starting from the right.</p>

