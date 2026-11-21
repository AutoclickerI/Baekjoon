# [Diamond V] ĐẾM - 11036 

[문제 링크](https://acmicpc.net/problem/11036) 

### 성능 요약

메모리: 231348 KB, 시간: 2522 ms

### 분류

자료 구조, 누적 합, 세그먼트 트리, 제곱근 분할법

### 제출 일자

2026년 11월 20일 23:58:28

### 문제 설명

<p>Cho một bảng hình chữ nhật kích thước N×M, ban đầu các phần tử trên bảng bằng 0. Có Q thao tác trên bảng như sau: </p>

<p>"1 a b x y w": tăng giá trị mỗi phần tử trong hình chữ nhật có góc trái dưới (a,b), góc phải trên (x,y) lên w đơn vị. </p>

<p>"2 a b x y": in ra tổng các phần tử trong hình chữ nhật có góc trái dưới (a,b), góc phải trên (x,y).</p>

### 입력 

 <p>Dòng đầu gồm 3 số N, M và Q. 1 ≤ N, M ≤ 1000. 1 ≤ Q ≤ 100000. Sau đó là Q dòng, mỗi dòng là 1 thao tác theo định dạng trên.</p>

### 출력 

 <p>Lần lượt với mỗi thao tác loại 2, in ra trên một dòng giá trị tính toán được.</p>

