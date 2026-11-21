# [Silver IV] Wlazł kotek na płotek - 8819 

[문제 링크](https://acmicpc.net/problem/8819) 

### 성능 요약

메모리: 81052 KB, 시간: 664 ms

### 분류

수학, 브루트포스 알고리즘, 정수론, 유클리드 호제법

### 제출 일자

2024년 9월 23일 16:19:50

### 문제 설명

<p>Wlazł kotek na płotek i skacze.</p>

<p>Płotek składa się z&nbsp;<strong>N</strong>&nbsp;sztachetek rozmieszczonych równomiernie na planie okręgu. Kotek skacze po płotku co&nbsp;<strong>K</strong>&nbsp;sztachetek ( czyli dla&nbsp;<strong>N</strong>&nbsp;= 8 i&nbsp;<strong>K</strong>&nbsp;= 3 kotek skacze kolejno na sztachetki: 1, 4, 7, 2, ... ). Kotek skacze tak długo, jak długo staje na sztachetkach, których jeszcze nie odwiedzał. Kiedy tylko dotrze do sztachetki na którą kiedyś już skoczył, od razu schodzi z płotka.</p>

<p>Znając liczbę sztachetek&nbsp;<strong>N</strong>&nbsp;wyznacz wszystkie możliwe&nbsp;<strong>K</strong>&nbsp;( 1 &lt;=&nbsp;<strong>K</strong>&nbsp;&lt;=&nbsp;<strong>N</strong>&nbsp;) dla których kotek skacząc w opisany wyżej sposób odwiedza wszystkie sztachetki w płocie.</p>

### 입력 

 <p>W pierwsze linii znajduje się liczba zestawów testowych&nbsp;<strong>Z</strong>&nbsp;( 1 &lt;=&nbsp;<strong>Z</strong>&nbsp;&lt;= 10). Następnie podawane są opisy kolejnych zestawów.</p>

<p>W jedynej linii zestawu znajduje się opisana w treści liczba naturalna&nbsp;<strong>N</strong>&nbsp;( 1 &lt;=&nbsp;<strong>N</strong>&nbsp;<strong>&nbsp;</strong>&lt;= 1000000&nbsp;).</p>

### 출력 

 <p>Dla każdego zestawu w osobnej linii wypisz wszystkie możliwe wartości&nbsp;<strong>K</strong>&nbsp;( zgodnie z opisem w treści ) w kolejności rosnącej, oddzielając kolejne liczby spacjami.</p>

