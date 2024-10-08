# [Silver III] Знания --- сила - 28968 

[문제 링크](https://www.acmicpc.net/problem/28968) 

### 성능 요약

메모리: 748508 KB, 시간: 1972 ms

### 분류

사칙연산, 다이나믹 프로그래밍, 수학

### 제출 일자

2024년 9월 20일 23:48:04

### 문제 설명

<p>Доктор Стрэндж активно изучает магию. Сегодня он наконец осознал, как распространяются темные силы. Оказывается, они распространяются с помощью так называемых <<носителей силы>>, носителями могут быть кто угодно --- люди, предметы, растения. А также каждый характеризуется своим <<уровнем>> --- количеством новых носителей, которых он может породить. Распространение происходит по следующему незамысловатому закону:</p>

<ul>
	<li>Изначально имеется $n$ носителей, все имеют уровень $1$.</li>
	<li>Каждый следующий день носитель уровня $i$ порождает новые $i$ носителей первого уровня, которые становятся активны только на следующий день.</li>
	<li>Сам же носитель переходит на новый уровень $i + 1$ (это означает, что на следующий день он породит уже $i + 1$ новых носителей) и его деятельность на текущий день прекращается.</li>
</ul>

<p>Всего в распоряжении Стрэнджа имеется $k$ дней. Его интересует, сколько всего носителей появится за это время. За помощью он обратился именно к вам.</p>

### 입력 

 <p>В единственной строке входного файла содержится два натуральных числа $n$ и $k$ --- количество носителей изначально и дней соответственно ($1 \le n \le 1000, 1 \le k \le 10^5$).</p>

### 출력 

 <p>Выведите одно число --- ответ на задачу. Так как ответ может получится слишком большим, выведите его по модулю $10^9 + 7$.</p>

