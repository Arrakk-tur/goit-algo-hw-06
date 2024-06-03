# goit-algo-hw-06

#### Аналіз основних характеристик (Вивід консолі):
- Кількість вершин: 5
- Кількість ребер: 7
- Ступені вершин:
  - Вершина 1 (Станція 1): 3
  - Вершина 2 (Станція 2): 3
  - Вершина 3 (Станція 3): 3
  - Вершина 4 (Станція 4): 3
  - Вершина 5 (Станція 5): 2

#### Шляхи у графі (Вивід консолі):
- Шлях за допомогою DFS:
[1, 2, 3, 4, 5]
- Шлях за допомогою BFS:
[1, 2, 5, 3, 4]


#### Порівняння результатів

**DFS:**
- Відвідує якомога глибше від поточної вершини перед поверненням.
- Результатом є шлях, який йде в глибину, перш ніж повернутись назад.
- У нашому прикладі DFS слідує шляхом 1 -> 2 -> 3 -> 4 -> 5.
- 
**BFS:**
- Відвідує всі сусіди поточної вершини перед переходом до наступного рівня.
- Результатом є шлях, який охоплює рівні одного за одним.
- У нашому прикладі BFS відвідує спершу всіх сусідів вершини 1 (2, 5, 3), а потім переходить до сусідів наступного рівня (4).

#### Найкоротші шляхи

- Найкоротші шляхи від вершини 1 (**Станція 1**):
	- до вершини 1 (Станція 1): шлях [1] з довжиною 0
	- до вершини 2 (Станція 2): шлях [1, 2] з довжиною 1.5
	- до вершини 5 (Станція 5): шлях [1, 5] з довжиною 2.2
	- до вершини 3 (Станція 3): шлях [1, 3] з довжиною 2.8
	- до вершини 4 (Станція 4): шлях [1, 2, 4] з довжиною 3.2
- Найкоротші шляхи від вершини 2 (**Станція 2**):
	- до вершини 2 (Станція 2): шлях [2] з довжиною 0
	- до вершини 1 (Станція 1): шлях [2, 1] з довжиною 1.5
	- до вершини 3 (Станція 3): шлях [2, 3] з довжиною 2.0
	- до вершини 4 (Станція 4): шлях [2, 4] з довжиною 1.7
	- до вершини 5 (Станція 5): шлях [2, 4, 5] з довжиною 2.7
- Найкоротші шляхи від вершини 3 (**Станція 3**):
	- до вершини 3 (Станція 3): шлях [3] з довжиною 0
	- до вершини 2 (Станція 2): шлях [3, 2] з довжиною 2.0
	- до вершини 4 (Станція 4): шлях [3, 4] з довжиною 2.5
	- до вершини 1 (Станція 1): шлях [3, 1] з довжиною 2.8
	- до вершини 5 (Станція 5): шлях [3, 4, 5] з довжиною 3.5
- Найкоротші шляхи від вершини 4 (**Станція 4**):
	- до вершини 4 (Станція 4): шлях [4] з довжиною 0
	- до вершини 3 (Станція 3): шлях [4, 3] з довжиною 2.5
	- до вершини 5 (Станція 5): шлях [4, 5] з довжиною 1.0
	- до вершини 2 (Станція 2): шлях [4, 2] з довжиною 1.7
	- до вершини 1 (Станція 1): шлях [4, 5, 1] з довжиною 3.2
- Найкоротші шляхи від вершини 5 (**Станція 5**):
	- до вершини 5 (Станція 5): шлях [5] з довжиною 0
	- до вершини 4 (Станція 4): шлях [5, 4] з довжиною 1.0
	- до вершини 1 (Станція 1): шлях [5, 1] з довжиною 2.2
	- до вершини 3 (Станція 3): шлях [5, 4, 3] з довжиною 3.5
	- до вершини 2 (Станція 2): шлях [5, 4, 2] з довжиною 2.7