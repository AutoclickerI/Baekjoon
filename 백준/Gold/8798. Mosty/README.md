# [Gold III] Mosty - 8798 

[문제 링크](https://www.acmicpc.net/problem/8798) 

### 성능 요약

메모리: 78572 KB, 시간: 3888 ms

### 분류

그래프 이론, 그리디 알고리즘, 위상 정렬, 방향 비순환 그래프

### 제출 일자

2025년 4월 2일 10:29:18

### 문제 설명

<p>W dwuwymiarowym królestwie Płaszczaków wszystkie ważne miejsca znajdują się w punktach postaci (<strong>X</strong>,0), gdzie <strong>X</strong> jest dodatnią liczbą całkowitą.</p>

<p>Niedawno król zarządził połączenie mostami <strong>N</strong> par ważnych miejsc. Most między punktami (<strong>A</strong>,0) i (<strong>B</strong>,0) to łamana składająca się z trzech odcinków: (<strong>A</strong>,0)-(<strong>A</strong>,<strong>P</strong>), (<strong>A</strong>,<strong>P</strong>)-(<strong>B</strong>,<strong>P</strong>), (<strong>B</strong>,<strong>P</strong>)-(<strong>B</strong>,0), gdzie <strong>P</strong> jest pewną dodatnią liczbą całkowitą nazywaną poziomem mostu. Wszystkie mosty muszą mieć różne poziomy będące liczbami od 1 do <strong>N</strong>. </p>

<p>Mosty mogą się przecinać, ale jest to sytuacja kłopotliwa technicznie. Jak przyporządkować poziomy do poszczególnych mostów, aby zminimalizować liczbę przecięć? Każde miejsce występuje na liście par co najwyżej raz.</p>

### 입력 

 <p>W pierwszej linii znajduje się jedna liczba naturalna <strong>Z</strong> ( <strong>Z</strong> = 1 ) oznaczająca liczbę zestawów testowych. W kolejnych liniach opisywane są kolejne zestawy.</p>

<p>W pierwszej linii zestawu znajduje się jedna liczba naturalna <strong>N </strong>( 1 <= <strong>N</strong> <= 5 000 ) oznaczająca liczbę par miejsc, które trzeba połączyć mostami. W kolejnych <strong>N </strong>liniach znajdują się po dwie liczby całkowite <strong>A</strong> i <strong>B</strong><strong> </strong>( 1 <= <strong>A</strong><strong> </strong>< <strong>B</strong> <= 2<strong>N</strong><strong> </strong>) oznaczające, że miejsca o współrzędnych (<strong>A</strong>,0), (<strong>B</strong>,0) należy połączyć mostem.</p>

### 출력 

 <p>W jednej linii należy wypisać, pooddzielane spacjami, numery kolejnych mostów posortowanych rosnąco według ich poziomów ( pierwszy ma być numer mostu o najmniejszym poziomie itd. ), minimalizujące liczbę przecięć. Numery mostów odpowiadają kolejności podanej na wejściu. W przypadku istnienia wielu rozwiązań minimalizujących liczbę przecięć należy podać leksykograficznie najmniejsze ( a więc to które minimalizuje numer mostu na poziomie 1, pośród tych rozwiązań to które minimalizuje numer mostu poziomie 2 itd., por. przykład ).</p>

