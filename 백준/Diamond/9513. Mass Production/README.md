# [Diamond V] Mass Production - 9513 

[문제 링크](https://www.acmicpc.net/problem/9513) 

### 성능 요약

메모리: 111496 KB, 시간: 156 ms

### 분류

그래프 이론, 최대 유량, 최소 비용 최대 유량

### 제출 일자

2026년 3월 9일 08:19:46

### 문제 설명

<p>Star Fleet needs to deploy a squadron of ships at the edge of Federation space. There is a nearby planet where the ships can be built, but the planet doesn’t have the infrastructure to support the construction of ships from scratch. It is, however, possible to assemble the ships using prefabricated kits containing an assortment of base parts. Each kit is designed to be turned into a ship by converting the base parts into the necessary ship components. To ensure consistent construction, parts from different kits should not be mixed and matched; each kit must be used in its entirety to construct exactly one ship. This squadron consists of two distinct classes of ships, Class A ships and Class B ships. Both classes consist of the same total number of components, though their individual makeup is different. Each base part is capable of being turned into any type of ship component, though the cost to turn a base part into a ship component varies depending on the base part type and the ship component type. You are responsible for creating these prefabricated kits, which must all be identical to each other. You have access to M5, the greatest computer of all time. What should the composition of the kit be to minimize the total cost of constructing the squadron?</p>

### 입력 

 <p>Input begins with a line with one integer T (1 ≤ T ≤ 50) denoting the number of test cases. Each test case begins with a line with four integers M, N, A, and B (1 ≤ M, N ≤ 10; 1 ≤ A, B ≤ 100), where M denotes the number of types of base parts, N denotes the number of types of ship components, A denotes the number of Class A ships required, and B denotes the number of Class B ships required. Next is a line with N integers a<sub>i</sub> denoting the quantity of ship component i needed for each Class A ship (0 ≤ a<sub>i</sub> ≤ 100). Next is a line with N integers b<sub>i</sub> denoting the quantity of ship component i needed for each Class B ship (0 ≤ b<sub>i</sub> ≤ 100; Σa<sub>i</sub> = Σb<sub>i</sub>). Next follow M lines with N integers c<sub>ij</sub> (0 ≤ c<sub>ij</sub> ≤ 100) denoting the cost of converting a single base part i into a single ship component j.</p>

### 출력 

 <p>For each test case, output a line with a single integer equal to the minimum total conversion cost of assembling all the ships from the factory kits.</p>

