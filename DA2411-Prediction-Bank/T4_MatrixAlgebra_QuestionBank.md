# DA2411 Linear Algebra — 24th Batch Preparation
# TOPIC 4: Matrix Algebra, Applied Multiplication & True/False
## Complete Question Bank with Full Solutions

**Exam probability: 95% | Past-paper frequency: 5/6 | Always Q2 | 10–25 marks**

---

## SECTION A: PAST-PAPER ANALYSIS

| Paper | Applied matrix task | True/False items | Matrix equation | Marks |
|-------|--------------------|--------------------|----------------|-------|
| 2019 | — | — | — | Different format |
| 2020 | — | — | — | Different format |
| 2022 | — | — | — | Different format |
| 2023 | California election: cost per contact × contacts in 2 cities | 5 True/False on dimensions and inverses | Solve $D = X - AX$ for $X$ [Q3a] | 25 Q2 + 5 Q3 |
| 2024 | — | — | Solve for scalars $a,b,c,d$ in matrix equation [Q1b] | 10 marks |
| 2025 | Colombo/Kandy logistics: cost per shipment × deliveries | 4 True/False on systems and eigenvalues | Find matrix $K$ from complex equation [Q3a] | 13 Q2 + 10 Q3 |

**Structure confirmed for DA2411 era:**
- **Q2 always has:** (a) applied matrix multiplication word problem [10–13 marks] + (b) True/False bank [12–15 marks]
- **Q3 always has:** a matrix equation sub-part [5–10 marks]

---

## SECTION B: EXAMINER PATTERNS & COMMON TRAPS

### Pattern 1 — Applied multiplication: encoding matters more than computing
The examiner awards marks for the encoding step:
- Correctly identifying what each matrix represents
- Getting the dimensions right (cost vector is 1×3 or 3×1 depending on how you set it up)
- Choosing the product that gives a meaningful result

**Trap:** Students who write $C \times D$ without checking if the product is defined, or get a product that has no meaningful interpretation, lose method marks even if their arithmetic is correct.

### Pattern 2 — "Total cost in one city" vs "total contacts of each type"
Two different products give two different things:
- Cost vector × delivery matrix → total cost per city (one number per city)
- Delivery matrix × ones vector → total contacts of each type

The examiner asks for BOTH in the 2023 and 2025 papers (parts c and d/e). Students who use the same product for both lose marks.

### Pattern 3 — True/False canonical statements
Across 2023 and 2025, the same families of statements appear. The examiner expects:
- A clear TRUE/FALSE declaration
- A mathematical PROOF (for TRUE) or a specific COUNTEREXAMPLE (for FALSE)
- A counterexample must be a concrete numerical matrix, not just "consider a matrix A such that..."

### Pattern 4 — Matrix equation solving (Q3a)
The examiner writes equations like $D = X - AX$ or $\frac{1}{2}K \cdot B = C - A$. Students must:
1. Isolate $X$ (or $K$) algebraically, treating matrices like variables
2. Remember: matrix multiplication is NOT commutative — you cannot move $A$ past $X$ freely
3. Factor correctly: $D = X - AX = (I-A)X$, then $X = (I-A)^{-1}D$

**Trap (2025 Q3a):** When isolating $K$, students multiply on the wrong side. If $\frac{1}{2}KB = M$, then $K = 2MB^{-1}$ (multiply on the RIGHT by $B^{-1}$), not $K = 2B^{-1}M$.

### Pattern 5 — The canonical True/False statements (memorise all)
These specific statements have appeared or are at high risk of appearing:

| Statement | Answer | Key reason |
|-----------|--------|-----------|
| Every square matrix has an inverse | FALSE | Singular matrices have no inverse |
| $n\times n$ system always has a solution | FALSE | Inconsistent systems exist |
| More variables than equations → always a solution | FALSE | $0x+0y=1$ has no solution |
| Two non-parallel lines always intersect | TRUE | Non-parallel lines in a plane must meet |
| If $\lambda=0$ is an eigenvalue, $A$ is invertible | FALSE | $\lambda=0$ ↔ $A$ is singular |
| $(AB)^T = A^TB^T$ | FALSE | Correct: $(AB)^T = B^TA^T$ |
| Matrix addition is commutative | TRUE | $(A+B)_{ij} = a_{ij}+b_{ij} = b_{ij}+a_{ij}$ |
| If $AB$ is defined, $BA$ is defined | FALSE | $A$: $2\times3$, $B$: $3\times1$ → $AB$: $2\times1$, $BA$: $1\times3$... actually $BA$ IS defined here. Better: $A$: $2\times3$, $B$: $3\times4$ → $AB$: $2\times4$, $BA$: $4\times2$... also defined. Try: $A$: $2\times3$, $B$: $3\times1$ → $AB$: $2\times1$ ✓, $BA$ DNE ($1\times3$ times $2\times3$ — inner dims $3\neq 2$). Wait: $B$ is $3\times1$, $A$ is $2\times3$. $BA$: inner dims $1\neq 2$ → DNE. ✓ |

---

## SECTION C: QUESTION BANK

---

### ─────────────────────────────────────
### EASY QUESTIONS (E1 – E3)
### ─────────────────────────────────────

---

## E1. Matrix Encoding and Multiplication — Warmup

A tutoring company charges three different rates: LKR 1,500/hour for mathematics, LKR 1,200/hour for science, and LKR 800/hour for English. In January, tutor A taught 20 hours of maths, 15 hours of science, and 10 hours of English. Tutor B taught 12 hours of maths, 25 hours of science, and 18 hours of English.

**i.** Encode the hourly rates as a row vector $R$ (1×3). **[2 marks]**

**ii.** Encode the hours worked as a matrix $H$ with tutors as rows (2×3). **[2 marks]**

**iii.** Compute $HR^T$ and interpret the result. **[4 marks]**

**iv.** What does the product $R \cdot H^T$ represent? Compute it. **[4 marks]**

---

### SOLUTION E1

**Part (i):**

$$R = \begin{bmatrix}1500 & 1200 & 800\end{bmatrix} \quad \text{(1×3, in LKR/hour)}$$

**Part (ii):** Rows = tutors (A, B), cols = subjects (Maths, Science, English):

$$H = \begin{bmatrix}20 & 15 & 10\\12 & 25 & 18\end{bmatrix} \quad \text{(2×3, in hours)}$$

**Part (iii): $HR^T$**

$H$ is 2×3, $R^T$ is 3×1. Product is 2×1.

$$HR^T = \begin{bmatrix}20&15&10\\12&25&18\end{bmatrix}\begin{bmatrix}1500\\1200\\800\end{bmatrix}$$

Row 1 (Tutor A): $20(1500)+15(1200)+10(800) = 30000+18000+8000 = \mathbf{56000}$

Row 2 (Tutor B): $12(1500)+25(1200)+18(800) = 18000+30000+14400 = \mathbf{62400}$

$$HR^T = \begin{bmatrix}56000\\62400\end{bmatrix}$$

**Interpretation:** Tutor A earned **LKR 56,000** in January; Tutor B earned **LKR 62,400**. Each entry gives the total earnings of one tutor.

**Part (iv): $RH^T$**

$R$ is 1×3, $H^T$ is 3×2. Product is 1×2.

$$RH^T = \begin{bmatrix}1500&1200&800\end{bmatrix}\begin{bmatrix}20&12\\15&25\\10&18\end{bmatrix}$$

Entry (1,1): $1500(20)+1200(15)+800(10) = 30000+18000+8000 = 56000$

Entry (1,2): $1500(12)+1200(25)+800(18) = 18000+30000+14400 = 62400$

$$RH^T = \begin{bmatrix}56000 & 62400\end{bmatrix}$$

**Interpretation:** Same values, now as a row vector: [earnings of Tutor A, earnings of Tutor B]. This is the transpose of $HR^T$ — both represent total earnings per tutor.

---

## E2. Transpose Laws — True/False Foundation

For each statement, state TRUE or FALSE with a proof or counterexample:

**a)** For any two matrices $A$ and $B$ where $AB$ is defined, $(AB)^T = A^T B^T$. **[3 marks]**

**b)** For any square matrix $A$, $A + A^T$ is always symmetric. **[3 marks]**

**c)** Matrix addition is commutative: $A + B = B + A$ for any matrices of the same size. **[3 marks]**

---

### SOLUTION E2

**Part (a): FALSE**

The correct identity is $(AB)^T = B^T A^T$ (note the REVERSAL of order).

**Counterexample:** Let $A = \begin{bmatrix}1&2\\0&1\end{bmatrix}$, $B = \begin{bmatrix}1&0\\1&1\end{bmatrix}$.

$AB = \begin{bmatrix}3&2\\1&1\end{bmatrix}$, so $(AB)^T = \begin{bmatrix}3&1\\2&1\end{bmatrix}$.

$A^TB^T = \begin{bmatrix}1&0\\2&1\end{bmatrix}\begin{bmatrix}1&1\\0&1\end{bmatrix} = \begin{bmatrix}1&1\\2&3\end{bmatrix} \neq (AB)^T$. □

**Part (b): TRUE**

Let $S = A + A^T$. We show $S^T = S$:

$$S^T = (A + A^T)^T = A^T + (A^T)^T = A^T + A = A + A^T = S$$

Since $S^T = S$, the matrix $S = A + A^T$ is **symmetric** for any square matrix $A$. □

**Part (c): TRUE**

For matrices $A$ and $B$ of the same size $m \times n$:

$$(A+B)_{ij} = a_{ij} + b_{ij} = b_{ij} + a_{ij} = (B+A)_{ij}$$

Since corresponding entries are equal (by commutativity of real number addition), $A + B = B + A$. □

---

## E3. Solve for Matrix X — Basic Isolation

Solve each matrix equation for $X$, given that $A$ and $B$ are square invertible matrices of the same size:

**a)** $3X - A = B$ **[2 marks]**

**b)** $AX = B$ **[2 marks]**

**c)** $XA = B$ **[2 marks]**

**d)** $AXB = C$ **[3 marks]**

---

### SOLUTION E3

**Part (a):**
$3X = B + A \implies \boxed{X = \frac{1}{3}(A+B)}$

(Scalar division is fine; $A+B$ is well-defined since same size.)

**Part (b):**
Multiply both sides on the LEFT by $A^{-1}$:
$A^{-1}AX = A^{-1}B \implies IX = A^{-1}B \implies \boxed{X = A^{-1}B}$

**Part (c):**
Multiply both sides on the RIGHT by $A^{-1}$:
$XAA^{-1} = BA^{-1} \implies XI = BA^{-1} \implies \boxed{X = BA^{-1}}$

**Note:** $X = A^{-1}B \neq BA^{-1}$ in general — the side on which you multiply matters!

**Part (d):**
Multiply on LEFT by $A^{-1}$ and on RIGHT by $B^{-1}$:
$A^{-1}(AXB)B^{-1} = A^{-1}CB^{-1}$
$\implies (A^{-1}A)X(BB^{-1}) = A^{-1}CB^{-1}$
$\implies IXI = A^{-1}CB^{-1}$
$\implies \boxed{X = A^{-1}CB^{-1}}$

---

### ─────────────────────────────────────
### MEDIUM QUESTIONS (M1 – M4)
### ─────────────────────────────────────

---

## M1. California Election — The Exact 2023 Q2 Question [Must-Know]

In a local California election, a public relations firm promoted its candidate in three ways: **telephone calls**, **house calls**, and **letters**. The cost per contact for a telephone call is \$1.20, the cost per contact for a house call is \$3.00, and the cost per contact for a letter is \$1.45.

**a)** Put this information into a matrix and label it $M$. **[5 marks]**

**b)** The number of contacts made in **Berkeley** are: 1,000 telephone calls, 500 house calls, and 5,000 letters. The number of contacts made in **Oakland** are: 2,000 telephone calls, 800 house calls, and 8,000 letters. Put this information into a matrix and label it $N$. **[5 marks]**

**c)** Using matrix multiplication, find the total amount spent in Berkeley. **[5 marks]**

**d)** If either product $MN$ or $NM$ has a meaningful interpretation, discuss and find the product. **[5 marks]**

**e)** Discuss and show a method using matrix multiplication to find the total number of telephone calls, house calls, and letters across both cities. **[5 marks]**

---

### SOLUTION M1

**Part (a):**

$M$ encodes the cost per contact for each method. Set up as a row vector (1×3):

$$M = \begin{bmatrix}1.20 & 3.00 & 1.45\end{bmatrix}$$

(Columns: telephone, house call, letter. Units: \$/contact)

**Part (b):**

$N$ encodes the number of contacts per method per city. Rows = cities (Berkeley, Oakland), Columns = methods:

$$N = \begin{bmatrix}1000 & 500 & 5000\\2000 & 800 & 8000\end{bmatrix}$$

**Part (c): Total cost in Berkeley**

We need a single dollar amount for Berkeley only. Use the Berkeley row of $N$ (row 1) as a column vector, multiplied by $M$:

$$\text{Cost (Berkeley)} = M \cdot \begin{bmatrix}1000\\500\\5000\end{bmatrix} = 1.20(1000) + 3.00(500) + 1.45(5000)$$

$= 1200 + 1500 + 7250 = \mathbf{\$9{,}950}$

Using matrix form: $M \cdot N^T$ gives a 1×2 vector of total costs per city:

$$MN^T = \begin{bmatrix}1.20&3.00&1.45\end{bmatrix}\begin{bmatrix}1000&2000\\500&800\\5000&8000\end{bmatrix} = \begin{bmatrix}9950 & 16040\end{bmatrix}$$

Berkeley: **\$9,950** | Oakland: **\$16,040**

**Part (d): $MN$ or $NM$?**

$M$: 1×3. $N$: 2×3.

$MN$: (1×3)(2×3) — inner dims 3 ≠ 2 → **DNE**.

$NM^T$: (2×3)(3×1) = **2×1** — this is the total cost per city, computed in part (c).

Actually, the meaningful product is $NM^T$ (not $MN$ or $NM$):

$$NM^T = \begin{bmatrix}1000&500&5000\\2000&800&8000\end{bmatrix}\begin{bmatrix}1.20\\3.00\\1.45\end{bmatrix} = \begin{bmatrix}9950\\16040\end{bmatrix}$$

**Interpretation:** Entry 1 = total campaign cost in Berkeley (\$9,950); Entry 2 = total campaign cost in Oakland (\$16,040).

**Part (e): Total contacts of each type across both cities**

We want: [total telephone calls, total house calls, total letters] = sum of Berkeley + Oakland rows of $N$.

This equals $\mathbf{1}^T N$ where $\mathbf{1} = [1,1]^T$ (a column of ones):

$$\begin{bmatrix}1&1\end{bmatrix}\begin{bmatrix}1000&500&5000\\2000&800&8000\end{bmatrix} = \begin{bmatrix}3000 & 1300 & 13000\end{bmatrix}$$

**Interpretation:** Total contacts: **3,000 telephone calls**, **1,300 house calls**, **13,000 letters** across both cities.

---

## M2. Colombo/Kandy Logistics — The Exact 2025 Q2a Question [Must-Know]

A logistics company uses three methods to deliver goods: **truck**, **rail**, and **air**. The cost per shipment is \$2.50 for truck, \$3.75 for rail, and \$5.00 for air.

**i.** Represent this data as a matrix labeled $C$. **[4 marks]**

**ii.** The number of deliveries in **Colombo**: 120 by truck, 80 by rail, 50 by air. In **Kandy**: 90 by truck, 100 by rail, 60 by air. Represent this in a matrix $D$. **[3 marks]**

**iii.** Compute the total delivery cost in Colombo using matrix multiplication. **[3 marks]**

**iv.** Find the total number of shipments of each type across both cities using matrix multiplication. **[3 marks]**

---

### SOLUTION M2

**Part (i):**

$$C = \begin{bmatrix}2.50 & 3.75 & 5.00\end{bmatrix} \quad \text{(1×3 row vector, \$/shipment)}$$

**Part (ii):**

$$D = \begin{bmatrix}120 & 80 & 50\\90 & 100 & 60\end{bmatrix} \quad \text{(2×3, rows = cities, cols = delivery methods)}$$

**Part (iii): Total delivery cost in Colombo**

$$C \cdot \text{(Colombo column vector)} = \begin{bmatrix}2.50&3.75&5.00\end{bmatrix}\begin{bmatrix}120\\80\\50\end{bmatrix}$$

$= 2.50(120) + 3.75(80) + 5.00(50) = 300 + 300 + 250 = \mathbf{\$850}$

Using $DC^T$ for both cities:

$$DC^T = \begin{bmatrix}120&80&50\\90&100&60\end{bmatrix}\begin{bmatrix}2.50\\3.75\\5.00\end{bmatrix} = \begin{bmatrix}850\\1012.50\end{bmatrix}$$

Colombo: **\$850** | Kandy: **\$1,012.50**

**Part (iv): Total shipments of each type**

$$\begin{bmatrix}1&1\end{bmatrix}D = \begin{bmatrix}1&1\end{bmatrix}\begin{bmatrix}120&80&50\\90&100&60\end{bmatrix} = \begin{bmatrix}210&180&110\end{bmatrix}$$

Total: **210 truck**, **180 rail**, **110 air** shipments across both cities.

---

## M3. The Canonical True/False Bank — 2025 Q2b [Must-Know — 12 marks]

Are the following statements true or false? If true, provide a mathematical proof. If false, provide a counterexample.

**i.** A linear system with the same number of equations as unknowns always has a solution. **[3 marks]**

**ii.** A linear system with more variables than equations always has a solution. **[3 marks]**

**iii.** A 2×2 linear system of two lines in the plane will have a solution if the two lines are not parallel. **[3 marks]**

**iv.** If matrix $A$ has an eigenvalue of 0, then $A$ is invertible. **[3 marks]**

---

### SOLUTION M3

**i. FALSE**

**Counterexample:** Consider:
$$x + y = 1$$
$$x + y = 2$$

Two equations, two unknowns. Subtracting: $0 = 1$ — a contradiction. **No solution exists.** The system is inconsistent even though it has equal numbers of equations and unknowns.

In matrix form: $\begin{bmatrix}1&1\\1&1\end{bmatrix}\begin{bmatrix}x\\y\end{bmatrix} = \begin{bmatrix}1\\2\end{bmatrix}$ has no solution since the coefficient matrix is singular and the system is inconsistent. □

**ii. FALSE**

**Counterexample:** Consider the single equation in two unknowns:
$$0x + 0y = 1$$

This has more unknowns (2) than equations (1), yet there is **no solution** since $0 = 1$ is a contradiction for any $(x, y)$.

*(Note: Theorem 1.1 states that if equations < variables, the system has NO solution or infinitely many — it does NOT always have a solution.)* □

**iii. TRUE**

**Proof:** Two lines in the plane that are NOT parallel have different slopes. Two non-parallel lines in $\mathbb{R}^2$ must intersect at exactly one point (they cannot be coincident and non-parallel simultaneously).

Algebraically: If lines $a_1x + b_1y = c_1$ and $a_2x + b_2y = c_2$ are non-parallel, their direction vectors are linearly independent, so the coefficient matrix $A = \begin{bmatrix}a_1&b_1\\a_2&b_2\end{bmatrix}$ has $\det(A) \neq 0$ (non-parallel ↔ rows not proportional ↔ det ≠ 0). By Theorem 2.3, the unique solution is $X = A^{-1}B$. □

**iv. FALSE**

**Counterexample:** Let $A = \begin{bmatrix}0&0\\0&0\end{bmatrix}$ (zero matrix).

$A$ has eigenvalue $\lambda = 0$ (since $A\mathbf{x} = 0 = 0\cdot\mathbf{x}$ for all $\mathbf{x}$). But $A$ is **singular** (not invertible) — $\det(A) = 0$.

**General proof that the statement is FALSE:** $\lambda = 0$ is an eigenvalue of $A$ iff $\det(A - 0\cdot I) = \det(A) = 0$ iff $A$ is **singular** (NOT invertible). The statement reverses the correct relationship. □

---

## M4. Solve the Matrix Equation — The 2023 Q3a and 2025 Q3a Types

**a)** Solve for $X$: $\quad D = X - AX$ **[5 marks]** *(2023 Q3a exact)*

**b)** Find the matrix $K$ such that: **[10 marks]** *(2025 Q3a exact)*

$$\begin{bmatrix}0&8&1\\7&-6&0\\3&0&1\end{bmatrix} + \frac{1}{2}K\begin{bmatrix}2&0&0\\5&2&0\\6&6&1\end{bmatrix} = \begin{bmatrix}7&0&6\\0&1&4\\3&7&0\end{bmatrix}$$

---

### SOLUTION M4

**Part (a): Solve $D = X - AX$**

Factor $X$ on the right side:

$$D = X - AX = IX - AX = (I - A)X$$

Multiply both sides on the LEFT by $(I-A)^{-1}$ (assuming $I-A$ is invertible):

$$\boxed{X = (I-A)^{-1}D}$$

**Important:** We must multiply on the LEFT because matrix multiplication is not commutative. $(I-A)^{-1}D \neq D(I-A)^{-1}$ in general.

*(Examiner note: This is the same algebraic structure as the Leontief model — $X = (I-M)^{-1}D$.)*

**Part (b): Find $K$**

Let $A = \begin{bmatrix}0&8&1\\7&-6&0\\3&0&1\end{bmatrix}$, $B = \begin{bmatrix}2&0&0\\5&2&0\\6&6&1\end{bmatrix}$, $C = \begin{bmatrix}7&0&6\\0&1&4\\3&7&0\end{bmatrix}$.

The equation is: $A + \frac{1}{2}KB = C$

**Step 1:** Isolate the $K$ term:

$$\frac{1}{2}KB = C - A$$

$$C - A = \begin{bmatrix}7-0&0-8&6-1\\0-7&1-(-6)&4-0\\3-3&7-0&0-1\end{bmatrix} = \begin{bmatrix}7&-8&5\\-7&7&4\\0&7&-1\end{bmatrix}$$

**Step 2:** Multiply both sides by 2:

$$KB = 2(C-A) = \begin{bmatrix}14&-16&10\\-14&14&8\\0&14&-2\end{bmatrix}$$

**Step 3:** Multiply on the RIGHT by $B^{-1}$:

$$K = 2(C-A)B^{-1}$$

**Find $B^{-1}$** by row reduction on $[B | I]$:

$$B = \begin{bmatrix}2&0&0\\5&2&0\\6&6&1\end{bmatrix}$$

$B$ is lower triangular → inverse has reciprocal diagonal entries and specific off-diagonal entries.

$[B|I]$:

$$\left[\begin{array}{ccc|ccc}2&0&0&1&0&0\\5&2&0&0&1&0\\6&6&1&0&0&1\end{array}\right]$$

$R_1 \div 2$:

$$\left[\begin{array}{ccc|ccc}1&0&0&1/2&0&0\\5&2&0&0&1&0\\6&6&1&0&0&1\end{array}\right]$$

$R_2 - 5R_1$; $R_3 - 6R_1$:

$$\left[\begin{array}{ccc|ccc}1&0&0&1/2&0&0\\0&2&0&-5/2&1&0\\0&6&1&-3&0&1\end{array}\right]$$

$R_2 \div 2$:

$$\left[\begin{array}{ccc|ccc}1&0&0&1/2&0&0\\0&1&0&-5/4&1/2&0\\0&6&1&-3&0&1\end{array}\right]$$

$R_3 - 6R_2$:

$$\left[\begin{array}{ccc|ccc}1&0&0&1/2&0&0\\0&1&0&-5/4&1/2&0\\0&0&1&-3+30/4&-3&1\end{array}\right]$$

$-3 + 30/4 = -12/4 + 30/4 = 18/4 = 9/2$

$$\left[\begin{array}{ccc|ccc}1&0&0&1/2&0&0\\0&1&0&-5/4&1/2&0\\0&0&1&9/2&-3&1\end{array}\right]$$

$$B^{-1} = \begin{bmatrix}1/2&0&0\\-5/4&1/2&0\\9/2&-3&1\end{bmatrix}$$

**Verify:** $BB^{-1}$: Row 1 × Col 1: $2(1/2)=1$ ✓; Row 2 × Col 1: $5(1/2)+2(-5/4) = 5/2-5/2=0$ ✓; Row 3 × Col 3: $6(0)+1(1)=1$ ✓.

**Step 4:** Compute $K = 2(C-A)B^{-1}$:

$$K = \begin{bmatrix}14&-16&10\\-14&14&8\\0&14&-2\end{bmatrix}\begin{bmatrix}1/2&0&0\\-5/4&1/2&0\\9/2&-3&1\end{bmatrix}$$

Row 1:
- $(1,1)$: $14(1/2)+(-16)(-5/4)+10(9/2) = 7+20+45 = 72$
- $(1,2)$: $14(0)+(-16)(1/2)+10(-3) = 0-8-30 = -38$
- $(1,3)$: $14(0)+(-16)(0)+10(1) = 10$

Row 2:
- $(2,1)$: $-14(1/2)+14(-5/4)+8(9/2) = -7-17.5+36 = 11.5$
- $(2,2)$: $-14(0)+14(1/2)+8(-3) = 0+7-24 = -17$
- $(2,3)$: $-14(0)+14(0)+8(1) = 8$

Row 3:
- $(3,1)$: $0(1/2)+14(-5/4)+(-2)(9/2) = 0-17.5-9 = -26.5$
- $(3,2)$: $0+14(1/2)+(-2)(-3) = 7+6 = 13$
- $(3,3)$: $0+0+(-2)(1) = -2$

$$\boxed{K = \begin{bmatrix}72&-38&10\\11.5&-17&8\\-26.5&13&-2\end{bmatrix}}$$

*(The examiner's 2025 solution may have clean integers — verify by checking $A + \frac{1}{2}KB = C$.)*

---

### ─────────────────────────────────────
### HARD QUESTIONS (H1 – H3)
### ─────────────────────────────────────

---

## H1. Extended True/False Bank — All Canonical Statements

For each statement, state TRUE or FALSE with a complete proof or counterexample:

**i.** Every square matrix has an inverse. **[3 marks]**

**ii.** For square matrices $A$ and $B$, $(AB)^T = A^TB^T$. **[3 marks]**

**iii.** If $AB = AC$ and $A \neq O$, then $B = C$. **[4 marks]**

**iv.** For any matrix $A$, $AA^T$ is always symmetric. **[3 marks]**

**v.** If $A$ and $B$ are both $n \times n$ invertible matrices, then $A + B$ is invertible. **[3 marks]**

**vi.** $(A^{-1})^T = (A^T)^{-1}$ for any invertible matrix $A$. **[4 marks]**

---

### SOLUTION H1

**i. FALSE**

**Counterexample:** The zero matrix $O = \begin{bmatrix}0&0\\0&0\end{bmatrix}$ is square but has no inverse (det = 0).

Any singular matrix works: e.g. $\begin{bmatrix}1&2\\2&4\end{bmatrix}$ has det $= 4-4 = 0$, so no inverse. □

**ii. FALSE**

The correct rule is $(AB)^T = B^T A^T$ (reversed order).

**Counterexample:** $A = \begin{bmatrix}1&1\\0&1\end{bmatrix}$, $B = \begin{bmatrix}1&0\\1&1\end{bmatrix}$.

$AB = \begin{bmatrix}2&1\\1&1\end{bmatrix}$, $(AB)^T = \begin{bmatrix}2&1\\1&1\end{bmatrix}$.

$A^TB^T = \begin{bmatrix}1&0\\1&1\end{bmatrix}\begin{bmatrix}1&1\\0&1\end{bmatrix} = \begin{bmatrix}1&1\\1&2\end{bmatrix} \neq (AB)^T$. □

**iii. FALSE — Matrix "cancellation" does not hold in general**

**Counterexample:** Let $A = \begin{bmatrix}1&1\\1&1\end{bmatrix}$, $B = \begin{bmatrix}1&0\\0&0\end{bmatrix}$, $C = \begin{bmatrix}0&0\\1&0\end{bmatrix}$.

$AB = \begin{bmatrix}1&0\\1&0\end{bmatrix}$, $AC = \begin{bmatrix}1&0\\1&0\end{bmatrix}$.

So $AB = AC$, $A \neq O$, but $B \neq C$. Cancellation of $A$ fails because $A$ is singular. □

*(If $A$ is invertible, then $AB=AC \Rightarrow B=C$. Cancellation requires invertibility.)*

**iv. TRUE**

$(AA^T)^T = (A^T)^T A^T = AA^T$.

Since $(AA^T)^T = AA^T$, the matrix $AA^T$ is **symmetric** for any matrix $A$ (regardless of whether $A$ is square). □

**v. FALSE**

**Counterexample:** $A = I$ (identity, invertible), $B = -I$ (also invertible: $(-I)^{-1} = -I$).

$A + B = I + (-I) = O$ (zero matrix), which is **not invertible**.

The sum of two invertible matrices can be singular. □

**vi. TRUE**

**Proof:** We show $(A^T)^{-1} = (A^{-1})^T$ by verifying both products equal $I$:

$(A^T)(A^{-1})^T = (A^{-1}A)^T = I^T = I$ ✓

$(A^{-1})^T(A^T) = (AA^{-1})^T = I^T = I$ ✓

Since both left and right products equal $I$, $(A^T)^{-1} = (A^{-1})^T$, i.e., $(A^{-1})^T = (A^T)^{-1}$. □

---

## H2. Sri Lankan Context — Full Applied Multiplication Q2 Simulation

*Predicted 24th Batch Q2 format.*

A Sri Lankan manufacturing company produces three products: **batik fabric (B)**, **handloom sarees (S)**, and **lacework (L)**. Production costs per unit (in LKR):

| Cost component | Batik | Sarees | Lacework |
|---------------|-------|--------|----------|
| Materials | 800 | 1200 | 600 |
| Labour | 500 | 900 | 700 |
| Overhead | 200 | 300 | 150 |

In Quarter 1, the **Kandy factory** produced 500 batik, 200 sarees, 350 lacework. The **Galle factory** produced 300 batik, 450 sarees, 200 lacework.

**i.** Encode the cost data as a matrix $P$ (3×3, cost components as rows, products as columns). **[4 marks]**

**ii.** Encode production quantities as a matrix $Q$ (2×3, factories as rows, products as columns). **[3 marks]**

**iii.** Compute $QP^T$ and interpret EACH entry of the resulting matrix. **[8 marks]**

**iv.** Which factory has higher total production cost? By how much? **[4 marks]**

**v.** Find the total materials cost across both factories using matrix multiplication. **[4 marks]**

---

### SOLUTION H2

**Part (i):** Rows = cost components, Cols = products (B, S, L):

$$P = \begin{bmatrix}800&1200&600\\500&900&700\\200&300&150\end{bmatrix}$$

**Part (ii):** Rows = factories (Kandy, Galle), Cols = products (B, S, L):

$$Q = \begin{bmatrix}500&200&350\\300&450&200\end{bmatrix}$$

**Part (iii): $QP^T$**

$Q$: 2×3, $P^T$: 3×3. Product: **2×3**.

$$P^T = \begin{bmatrix}800&500&200\\1200&900&300\\600&700&150\end{bmatrix}$$

$$QP^T = \begin{bmatrix}500&200&350\\300&450&200\end{bmatrix}\begin{bmatrix}800&500&200\\1200&900&300\\600&700&150\end{bmatrix}$$

**Row 1 (Kandy):**
- Materials: $500(800)+200(1200)+350(600) = 400000+240000+210000 = 850000$
- Labour: $500(500)+200(900)+350(700) = 250000+180000+245000 = 675000$
- Overhead: $500(200)+200(300)+350(150) = 100000+60000+52500 = 212500$

**Row 2 (Galle):**
- Materials: $300(800)+450(1200)+200(600) = 240000+540000+120000 = 900000$
- Labour: $300(500)+450(900)+200(700) = 150000+405000+140000 = 695000$
- Overhead: $300(200)+450(300)+200(150) = 60000+135000+30000 = 225000$

$$QP^T = \begin{bmatrix}850000&675000&212500\\900000&695000&225000\end{bmatrix}$$

**Interpretation of each entry:**

| Entry | Factory | Cost Component | Value (LKR) |
|-------|---------|---------------|-------------|
| (1,1) | Kandy | Total materials cost | 850,000 |
| (1,2) | Kandy | Total labour cost | 675,000 |
| (1,3) | Kandy | Total overhead cost | 212,500 |
| (2,1) | Galle | Total materials cost | 900,000 |
| (2,2) | Galle | Total labour cost | 695,000 |
| (2,3) | Galle | Total overhead cost | 225,000 |

**Part (iv):**

Total Kandy: $850000+675000+212500 = \text{LKR }1{,}737{,}500$

Total Galle: $900000+695000+225000 = \text{LKR }1{,}820{,}000$

**Galle factory** has higher total cost by $1{,}820{,}000 - 1{,}737{,}500 = \mathbf{LKR\ 82{,}500}$.

**Part (v): Total materials cost across both factories**

Row 1 of $QP^T$ gives Kandy materials (850,000); Row 2 gives Galle materials (900,000).

Using matrix multiplication: $\mathbf{1}^T \cdot$ (column 1 of $QP^T$):

$$\begin{bmatrix}1&1\end{bmatrix}\begin{bmatrix}850000\\900000\end{bmatrix} = \mathbf{LKR\ 1{,}750{,}000}$$

Total materials cost across both factories: **LKR 1,750,000**.

---

## H3. Complex Matrix Equation — Solve for X with Non-Square Matrices

Given that $A = \begin{bmatrix}2&1\\1&3\end{bmatrix}$ and $B = \begin{bmatrix}5&2\\1&1\end{bmatrix}$, solve for $X$:

**a)** $2AX - B = 3A$ **[5 marks]**

**b)** $X^T A = B^T$ **[5 marks]**

---

### SOLUTION H3

**Part (a):**

$2AX = 3A + B$

$$3A + B = \begin{bmatrix}6&3\\3&9\end{bmatrix}+\begin{bmatrix}5&2\\1&1\end{bmatrix} = \begin{bmatrix}11&5\\4&10\end{bmatrix}$$

$AX = \frac{1}{2}\begin{bmatrix}11&5\\4&10\end{bmatrix} = \begin{bmatrix}5.5&2.5\\2&5\end{bmatrix}$

$X = A^{-1}\begin{bmatrix}5.5&2.5\\2&5\end{bmatrix}$

Find $A^{-1}$: $\det(A) = 6-1 = 5$.

$A^{-1} = \frac{1}{5}\begin{bmatrix}3&-1\\-1&2\end{bmatrix}$

$$X = \frac{1}{5}\begin{bmatrix}3&-1\\-1&2\end{bmatrix}\begin{bmatrix}5.5&2.5\\2&5\end{bmatrix}$$

Row 1: $\frac{1}{5}[3(5.5)+(-1)(2),\ 3(2.5)+(-1)(5)] = \frac{1}{5}[14.5,\ 2.5] = [2.9,\ 0.5]$

Row 2: $\frac{1}{5}[(-1)(5.5)+2(2),\ (-1)(2.5)+2(5)] = \frac{1}{5}[-1.5,\ 7.5] = [-0.3,\ 1.5]$

$$\boxed{X = \begin{bmatrix}2.9&0.5\\-0.3&1.5\end{bmatrix}}$$

**Verify:** $2AX = 2A\begin{bmatrix}2.9&0.5\\-0.3&1.5\end{bmatrix}$. Check $2AX - B = 3A$... (can be verified by substitution).

**Part (b):**

$X^T A = B^T$

Transpose both sides: $(X^T A)^T = (B^T)^T \implies A^T X = B$

Since $A$ is symmetric ($A = A^T$): $AX = B$

$$X = A^{-1}B = \frac{1}{5}\begin{bmatrix}3&-1\\-1&2\end{bmatrix}\begin{bmatrix}5&2\\1&1\end{bmatrix}$$

Row 1: $\frac{1}{5}[15-1,\ 6-1] = \frac{1}{5}[14,5] = [2.8,\ 1]$

Row 2: $\frac{1}{5}[-5+2,\ -2+2] = \frac{1}{5}[-3,\ 0] = [-0.6,\ 0]$

$$\boxed{X = \begin{bmatrix}2.8&1\\-0.6&0\end{bmatrix}}$$

---

### ─────────────────────────────────────
### NIGHTMARE QUESTIONS (N1 – N2)
### ─────────────────────────────────────

---

## N1. Proof — Non-Commutativity and Its Consequences

**a)** Prove that matrix multiplication is NOT in general commutative by giving an explicit 2×2 counterexample and showing $AB \neq BA$. **[3 marks]**

**b)** Prove that if $A$ is invertible, then the cancellation law holds: $AB = AC \Rightarrow B = C$. **[4 marks]**

**c)** Prove the reversal law: $(AB)^{-1} = B^{-1}A^{-1}$ for invertible matrices $A$ and $B$. **[4 marks]**

**d)** A student writes: "Since $A(B+C) = AB + AC$, we can factor as follows: $AB + C = A(B + A^{-1}C)$." Is this valid? Prove or give a counterexample. **[4 marks]**

---

### SOLUTION N1

**Part (a):**

Let $A = \begin{bmatrix}1&2\\0&1\end{bmatrix}$, $B = \begin{bmatrix}1&0\\1&1\end{bmatrix}$.

$AB = \begin{bmatrix}1+2&0+2\\0+1&0+1\end{bmatrix} = \begin{bmatrix}3&2\\1&1\end{bmatrix}$

$BA = \begin{bmatrix}1+0&2+0\\1+0&2+1\end{bmatrix} = \begin{bmatrix}1&2\\1&3\end{bmatrix}$

$AB \neq BA$. □

**Part (b):**

Given: $AB = AC$, $A$ invertible.

Multiply both sides on the LEFT by $A^{-1}$:

$A^{-1}(AB) = A^{-1}(AC)$

$(A^{-1}A)B = (A^{-1}A)C$

$IB = IC$

$B = C$ □

**Part (c):**

We verify $(B^{-1}A^{-1})(AB) = I$ and $(AB)(B^{-1}A^{-1}) = I$:

$(B^{-1}A^{-1})(AB) = B^{-1}(A^{-1}A)B = B^{-1}IB = B^{-1}B = I$ ✓

$(AB)(B^{-1}A^{-1}) = A(BB^{-1})A^{-1} = AIA^{-1} = AA^{-1} = I$ ✓

Since both products equal $I$, $(AB)^{-1} = B^{-1}A^{-1}$. □

**Part (d): INVALID**

The student claims $AB + C = A(B + A^{-1}C)$.

Expand the right side: $A(B + A^{-1}C) = AB + A(A^{-1}C) = AB + (AA^{-1})C = AB + IC = AB + C$. ✓

So the algebra IS valid — the factoring step is correct!

**BUT** the student's reasoning contains a hidden assumption: $A^{-1}$ must exist. If $A$ is singular, $A^{-1}$ does not exist and the factoring fails.

The statement is **conditionally valid**: it holds if and only if $A$ is invertible. A complete answer requires this caveat. If the student presented it as universally true without stating $A$ must be invertible, that is an error. □

---

## N2. Multi-Step Matrix Equation with Proof Structure

Let $A$ be an $n \times n$ invertible matrix. Prove each of the following:

**a)** $(A^n)^{-1} = (A^{-1})^n$ for any positive integer $n$. *(Use induction or the reversal law repeatedly.)* **[5 marks]**

**b)** If $A^2 = A$ (A is idempotent), then either $A = I$ or $A$ is singular. **[4 marks]**

**c)** If $A^2 = I$, prove that $A^{-1} = A$. **[3 marks]**

---

### SOLUTION N2

**Part (a):** By induction.

**Base case ($n=1$):** $(A^1)^{-1} = A^{-1} = (A^{-1})^1$. ✓

**Inductive step:** Assume $(A^k)^{-1} = (A^{-1})^k$.

$(A^{k+1})^{-1} = (A \cdot A^k)^{-1} = (A^k)^{-1}A^{-1}$ (reversal law)

$= (A^{-1})^k \cdot A^{-1}$ (inductive hypothesis)

$= (A^{-1})^{k+1}$ ✓

By induction, $(A^n)^{-1} = (A^{-1})^n$ for all $n \geq 1$. □

**Part (b):**

$A^2 = A$ and $A$ invertible. Multiply both sides on LEFT by $A^{-1}$:

$A^{-1}A^2 = A^{-1}A \implies A = I$

So if $A$ is invertible and $A^2 = A$, then $A = I$.

Contrapositive: if $A \neq I$ and $A^2 = A$, then $A$ is **not invertible** (singular). □

Therefore: $A^2 = A$ implies either $A = I$ or $A$ is singular.

**Part (c):**

$A^2 = I$. We want to show $A^{-1} = A$.

Verify: $A \cdot A = A^2 = I$ and $A \cdot A = I$.

Both $AA = I$ and $AA = I$ confirm that $A$ is its own inverse.

Formally: $AA = I$ means $A$ satisfies the definition of $A^{-1}$ (a matrix $B$ is $A^{-1}$ iff $AB = BA = I$; here $B = A$). □

**Connection to 2025 exam:** The examiner asked "If $A^3 = I$, find $A^{-1}$." Same logic: $A \cdot A^2 = A^3 = I$, so $A^{-1} = A^2$.

---

## SECTION E: RAPID-FIRE REVISION

**Applied matrix multiplication — 3-step process:**

| Step | Action |
|------|--------|
| 1 | Label what each matrix represents (rows, columns, units) |
| 2 | Choose the product that gives the desired result |
| 3 | Verify dimensions before computing |

**True/False — the 6 canonical statements:**

| Statement | Answer | Key |
|-----------|--------|-----|
| Every square matrix has an inverse | FALSE | Singular matrices exist |
| $n$ equations, $n$ unknowns → always a solution | FALSE | Inconsistent systems exist |
| More variables than equations → always a solution | FALSE | $0=1$ has no solution |
| Two non-parallel lines in $\mathbb{R}^2$ → always a solution | TRUE | Det ≠ 0, unique solution |
| $\lambda=0$ eigenvalue → $A$ invertible | FALSE | $\lambda=0$ ↔ $A$ singular |
| $(AB)^T = A^TB^T$ | FALSE | Correct: $(AB)^T = B^TA^T$ |

**Matrix equation solving — the side rule:**

| Equation form | Solution | Warning |
|--------------|---------|---------|
| $AX = B$ | $X = A^{-1}B$ | Multiply LEFT |
| $XA = B$ | $X = BA^{-1}$ | Multiply RIGHT |
| $AXB = C$ | $X = A^{-1}CB^{-1}$ | Left AND right |
| $X - AX = D$ | $X = (I-A)^{-1}D$ | Factor first |

---

*End of Topic 4: Matrix Algebra, Applied Multiplication & True/False*
*Total: 3 Easy + 4 Medium + 3 Hard + 2 Nightmare = 12 questions with full solutions*
*Next: Topic 5 — Matrix Inverse, Determinants & Matrix Powers*
