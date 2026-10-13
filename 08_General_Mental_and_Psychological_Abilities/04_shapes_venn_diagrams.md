# Geometric Shapes, Sub-sections, Counting of Figures & Venn Diagrams

**Topic ID:**  | **Subject:** General Mental and Psychological Abilities | **Paper:** Screening Paper-II (Section A)

**Syllabus Mapping:** Shapes and their Sub-sections, Venn Diagram - Counting of Triangles, Squares, Rectangles and Parallelograms, Embedded Figures, Paper Folding and Cutting, Two-Set and Three-Set Venn Diagrams, Set Theory Formulations.

---


# Spatial Geometry, Counting of Geometric Figures, Sub-sections, and Venn Diagram Set Formulations


Geometric visualization and set-theoretic Venn diagrams evaluate non-verbal spatial aptitude and logical grouping. Counting nested triangles and rectangles requires systematic algebraic formulas rather than manual tallying to prevent omission or double-counting.


## 1. Mathematical Formulas for Counting Geometric Figures


### Table: Formulas and Shortcuts for Counting Figures

| Figure Type | Geometric Configuration | Direct Shortcut Formula | Example Calculation |
| --- | --- | --- | --- |
| Triangles in a Divided Triangle | Vertical lines from vertex dividing base into $n$ parts. | Total Triangles = $\frac{n(n+1)}{2}$ | If base is divided into 4 segments: $\frac{4 \times 5}{2} = 10$ triangles. |
| Triangles inside a Quadrilateral | Square or rectangle with both diagonals intersecting, divided into $n$ smaller triangles. | Total Triangles = $2n$ | An 8-part divided square has $2 \times 8 = 16$ triangles. |
| Squares in an $m \times n$ Grid | Grid of $m$ rows and $n$ columns (where $m \le n$). | $\sum (m \times n) + (m-1)(n-1) + ...$ | In a $4 \times 4$ chessboard: $4^2 + 3^2 + 2^2 + 1^2 = 16+9+4+1 = 30$ squares. |
| Rectangles in an $m \times n$ Grid | Grid with $m$ rows and $n$ columns. | Total Rectangles = $\left[\frac{m(m+1)}{2}\right] \times \left[\frac{n(n+1)}{2}\right]$ | In a $3 \times 3$ grid: $\frac{3 \times 4}{2} \times \frac{3 \times 4}{2} = 6 \times 6 = 36$ rectangles (including squares). |



## 2. Set Theory Formulations for 2-Set and 3-Set Venn Diagrams

* Two-Set Union Formula: $n(A \cup B) = n(A) + n(B) - n(A \cap B)$.

* Only A: $n(A) - n(A \cap B)$.

* Three-Set Union Formula: $n(A \cup B \cup C) = n(A) + n(B) + n(C) - n(A \cap B) - n(B \cap C) - n(A \cap C) + n(A \cap B \cap C)$.

* Exactly Two Sets: $[n(A \cap B) + n(B \cap C) + n(A \cap C)] - 3 \cdot n(A \cap B \cap C)$.

* Exactly One Set: $n(A) + n(B) + n(C) - 2[n(A \cap B) + n(B \cap C) + n(A \cap C)] + 3 \cdot n(A \cap B \cap C)$.




## Previous Years Questions (PYQs) - APPSC Group-1


### Part A: Analytical Descriptive Set Formulation

1. In a survey of 500 aspirants preparing for APPSC Group-1: 240 read Newspaper A (The Hindu), 200 read Newspaper B (Eenadu), and 180 read Newspaper C (Indian Express). 70 read both A and B, 60 read both B and C, and 50 read both A and C. 30 read all three newspapers. Determine:
(i) How many aspirants read exactly one newspaper?
(ii) How many read at least two newspapers?
(iii) How many aspirants read none of the three newspapers?
(APPSC Group-1 Mains Analytical, 10 Marks)
-> Model Approach: Use set formulations where Total N = 500, n(A)=240, n(B)=200, n(C)=180, n(A∩B)=70, n(B∩C)=60, n(A∩C)=50, and n(A∩B∩C)=30.
Total reading at least one: n(A∪B∪C) = 240 + 200 + 180 - (70 + 60 + 50) + 30 = 620 - 180 + 30 = 470.
(i) Exactly one newspaper = n(A∪B∪C) - [Exactly two + All three] = 470 - [(70-30)+(60-30)+(50-30) + 30] = 470 - [40 + 30 + 20 + 30] = 470 - 120 = 350.
(ii) At least two newspapers = Exactly two + All three = (40 + 30 + 20) + 30 = 120.
(iii) None of the three newspapers = Total - n(A∪B∪C) = 500 - 470 = 30 aspirants.




### Part B: Screening / Prelims Objective Questions

* Q1. How many total triangles are present in a square whose diagonals and medians intersect, dividing the interior into 8 elementary triangular sectors?
(a) 12
(b) 14
(c) 16
(d) 18
Correct Answer: (c) 16 [Explanation: In any quadrilateral with diagonals intersecting, the total number of triangles is 2n, where n is the number of small internal triangles. Here n = 8, so Total = 2 * 8 = 16 triangles.]

* Q2. How many total rectangles (including squares) are present in a standard 8x8 chessboard?
(a) 204
(b) 1,296
(c) 1,024
(d) 512
Correct Answer: (b) 1,296 [Explanation: Total rectangles in an m x n grid is given by [m(m+1)/2] * [n(n+1)/2]. For an 8x8 chessboard: [8*9/2] * [8*9/2] = 36 * 36 = 1,296 rectangles.]

* Q3. In a town of 100 families, 65 families have cars, 45 have motorcycles, and 15 families have neither. How many families have both a car and a motorcycle?
(a) 20
(b) 25
(c) 30
(d) 35
Correct Answer: (b) 25 [Explanation: Families having at least one vehicle = 100 - 15 = 85. Using n(A∪B) = n(A) + n(B) - n(A∩B): 85 = 65 + 45 - n(A∩B) => 85 = 110 - n(A∩B) => n(A∩B) = 110 - 85 = 25 families.]

* Q4. Which of the following Venn diagrams best represents the relationship between: 'Judges, Thieves, and Criminals'?
(a) Three disjoint circles
(b) One circle inside another, with the third circle disjoint
(c) Two concentric circles intersecting a third circle
(d) One circle completely containing the other two
Correct Answer: (b) One circle inside another, with the third circle disjoint [Explanation: All thieves are criminals (so Thieves is completely inside Criminals). Judges are legally separate and distinct from criminals, forming a disjoint circle.]

* Q5. How many total squares are there in an 8x8 chessboard?
(a) 64
(b) 128
(c) 204
(d) 1,296
Correct Answer: (c) 204 [Explanation: Total squares in an n x n grid is given by sum of squares of first n natural numbers: n(n+1)(2n+1)/6. For n=8: (8 * 9 * 17)/6 = 1,224 / 6 = 204 squares.]


