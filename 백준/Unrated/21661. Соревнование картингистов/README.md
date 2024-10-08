# [Unrated] Соревнование картингистов - 21661 

[문제 링크](https://www.acmicpc.net/problem/21661) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

구현, 문자열

### 제출 일자

2024년 9월 27일 12:50:20

### 문제 설명

<p>После очередного этапа чемпионата мира по кольцевым автогонкам на автомобилях с открытыми колесами Формула-А гонщики собрались вместе в кафе, чтобы обсудить полученные результаты. Они вспомнили, что в молодости соревновались не на больших болидах, а на картах – спортивных автомобилях меньших размеров.</p>

<p>Друзья решили выяснить победителя в одной из гонок на картах. Победителем гонки являлся тот гонщик, у которого суммарное время прохождения всех кругов трассы было минимальным.</p>

<p>Поскольку окончательные результаты не сохранились, то каждый из n участников той гонки вспомнил и выписал результаты прохождения каждого из m кругов трассы. К сожалению, гонщикам было сложно вычислить победителя той гонки. В связи с этим они попросили сделать это вас. </p>

<p>Требуется написать программу, которая вычислит победителя гонки на картах, о которой говорили гонщики.</p>

### 입력 

 <p>Первая строка входного файла содержит два целых числа n и m (1 ≤ n, m ≤ 100). Последующие 2∙n строк описывают прохождение трассы каждым из участников. Описание прохождения трассы участником состоит из двух строк. Первая строка содержит имя участника с использованием только латинских букв (строчных и заглавных). Имена всех участников различны, строчные и заглавные буквы в именах различаются. </p>

<p>Вторая строка содержит m положительных целых чисел, где каждое число – это время прохождения данным участником каждого из m кругов трассы (каждое из этих чисел не превосходит 1000). Длина каждой строки не превышает 255 символов. </p>

### 출력 

 <p>В выходной файл необходимо вывести имя победителя гонки на картах. Если победителей несколько, требуется вывести имя любого из них.</p>

