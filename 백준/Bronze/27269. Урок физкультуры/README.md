# [Bronze I] Урок физкультуры - 27269 

[문제 링크](https://www.acmicpc.net/problem/27269) 

### 성능 요약

메모리: 31120 KB, 시간: 32 ms

### 분류

구현, 정렬

### 제출 일자

2024년 10월 11일 19:09:18

### 문제 설명

<p>На уроке физкультуры тренер Андрей Сергеевич выстраивает учеников в одну шеренгу. В шеренге сначала идут мальчики, а потом девочки. При этом мальчики в шеренге стоят по убыванию роста, аналогично девочки тоже стоят по убыванию роста. Таким образом, следом за самым низким мальчиком стоит самая высокая девочка.</p>

<p>Андрея Сергеевича заинтересовал вопрос, какое максимальное различие в росте двух стоящих рядом учеников. Напишете программу, которая поможет Андрею Сергеевичу ответить на этот важный для него вопрос.</p>

### 입력 

 <p>Первая строка содержит целое число $n$ --- число учеников в классе ($2 \le n \le 50$). Следующие $n$ строк содержат по два целых числа каждая: $a_i$ и $h_i$ --- пол и рост в сантиметрах $i$-го ученика ($a_i$ равно 0 или 1, $100 \le h_i \le 200$). Значение $a_i = 0$ означает, что $i$-й ученик --- мальчик, а значение $a_i = 1$ означает, что $i$-й ученик --- девочка.</p>

### 출력 

 <p>Выведите одно число --- максимальное различие в росте стоящих рядом учеников после того, как они выстроятся в шеренгу на уроке физкультуры.</p>

