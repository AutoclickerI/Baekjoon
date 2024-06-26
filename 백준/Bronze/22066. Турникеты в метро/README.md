# [Bronze I] Турникеты в метро - 22066 

[문제 링크](https://www.acmicpc.net/problem/22066) 

### 성능 요약

메모리: 39852 KB, 시간: 2584 ms

### 분류

구현, 시뮬레이션

### 제출 일자

2024년 4월 13일 15:11:23

### 문제 설명

<p>Вася и Петя каждый день ездят на метро, поэтому они решили купить себе проездные карты, чтобы каждый раз не покупать жетон. Каждая карта может использоваться в течение определенного количества дней, после чего она становится неактивной.</p>

<p>При каждом проходе через турникет высвечивается, сколько еще дней карта может быть использована (включая текущий день). Но, к сожалению, табло, на котором это количество дней отображается, может показывать только однозначные и двузначные числа. Если же в отображаемом числе хотя бы три цифры, на табло покажется число 99. Например, если на карте осталось 5 дней, то на турникете покажется число 5, если 12 дней, то число 12, а если 123 дня, то на турникете покажется число 99. Если на карте остается 0 дней, она становится неактивной и по ней больше нельзя проходить через турникет.</p>

<p>Сейчас у Васи на карте осталось <i>a</i> дней, а у Пети — <i>b</i>. Они каждый день ездят на метро и каждый день смотрят на числа, которые отображаются на турникете. И им стало интересно: через сколько дней в первый раз число на турникете у одного из них будет ровно в <i>k</i> раз больше, чем число на турникете у другого. Помогите друзьям выяснить ответ на этот вопрос.</p>

### 입력 

 <p>Первая строка входных данных содержит одно число <i>t</i> (1 ≤ <i>t</i> ≤ 100000) — количество тестов. Следующие <i>t</i> строк содержат по тесту каждая. Каждый тест задается тремя целыми числами: <i>a</i>, <i>b</i>, <i>k</i> (1 ≤ <i>a</i>, <i>b</i> ≤ 2·10<sup>9</sup>, 1 ≤ <i>k</i> ≤ 100) — количество оставшихся дней на карточках у Васи и Пети и требуемое отношение.</p>

### 출력 

 <p>Для каждого набора данных выведите единственное число: через сколько дней у одного из друзей на турникете будет показано в <i>k</i> раз больше поездок, чем у другого. Если такого не произойдет до того дня, когда у одного из друзей карта станет неактивной, выведите «<code>-1</code>».</p>

