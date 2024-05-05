# [Silver IV] Śpiew - 8575 

[문제 링크](https://www.acmicpc.net/problem/8575) 

### 성능 요약

메모리: 43704 KB, 시간: 88 ms

### 분류

그리디 알고리즘, 수학

### 제출 일자

2024년 5월 5일 23:41:55

### 문제 설명

<p>Na lekcji śpiewu uczniowie Bajtazara siedzą w jednym, długim rzędzie. Nie wszystkie krzesła są w nim zapełnione i pomiędzy poszczególnymi uczniami mogą występować wolne miejsca.</p>

<p>Na lekcji uczniowie potrzebują śpiewników, ale nie każdy musi trzymać śpiewnik. Nauczyciel musi się zatroszczyć tylko o to, aby każdy uczeń bez śpiewnika siedział bezpośrednio obok ucznia ze śpiewnikiem. Ponieważ uczniowie na każdej lekcji siadają w inny sposób a śpiewników jest dosyć mało, Bajtazar poprosił Ciebie, swojego przyjaciela, o napisanie programu, który dla danego rozmieszczenia uczniów wyznaczy minimalną liczbę potrzebnych im śpiewników, aby ułatwić Bajtazarowi rozdawanie śpiewników.</p>

### 입력 

 <p>W pierwszym wierszu standardowego wejścia znajduje się jedna liczba naturalna $n$ ($1 ≤ n ≤ 1\,000\,000$) oznaczająca liczbę miejsc w rzędzie. W drugim wierszu znajduje się ciąg $n$ znaków opisujących kolejne miejsca:</p>

<ul>
	<li>znak "<code>W</code>" oznacza miejsce wolne,</li>
	<li>znak "<code>Z</code>" oznacza miejsce zajęte przez ucznia.</li>
</ul>

### 출력 

 <p>Twój program powinien wypisać na wyjście jedną liczbę całkowitą oznaczającą minimalną liczbę śpiewników, które można rozdać uczniom tak, aby każdy miał śpiewnik lub siedział obok kogoś ze śpiewnikiem.</p>

