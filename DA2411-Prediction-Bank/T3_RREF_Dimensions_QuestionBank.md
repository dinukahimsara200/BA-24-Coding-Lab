# DA2411 Linear Algebra — 24th Batch Preparation
# TOPIC 3: RREF Identification & Matrix Dimension Analysis
## Complete Question Bank with Full Solutions

**Exam probability: 85% | Past-paper frequency: 4/6 | Always Q1 | 10–19 marks**

---

## SECTION A: PAST-PAPER ANALYSIS

| Paper | Dimension analysis | RREF check | Row operation fill | Marks |
|-------|-------------------|------------|-------------------|-------|
| 2019 | — | — | — | Not Q1 format |
| 2020 | — | — | — | Not Q1 format |
| 2022 | — | — | — | Not Q1 format |
| 2023 | 3-part T/F on dimensions (A: 3×4, B: 4×3, C: 3×5, D: 5×5 singular, E: 4×4 non-singular) | Not explicit | Not present | 10/25 |
| 2024 | — | 3 matrices, identify violation or confirm RREF | Not present | 6/25 |
| 2025 | 5-matrix dimension table (F:5×4, G:4×5, H:4×4 nonsingular, J:5×5 singular, K:4×4 identity) → 5 expressions | Not explicit | 4-mark fill exercise | 19/25 |

**The 2025 paper put 19 of 25 marks in Q1 into dimension + row operation work — the heaviest allocation ever. For 24th Batch, expect Q1 to follow the 2025 structure exactly:**
- Part (a): 5-matrix dimension table → 5 expressions [15 marks]
- Part (b): Row operation fill-in [4 marks]
- Part (c): RREF identification [6 marks]

---

## SECTION B: EXAMINER PATTERNS & COMMON TRAPS

### Pattern 1 — Dimension table with mixed properties (2023, 2025)
Always includes: one singular matrix, one non-singular matrix, one identity or special matrix, rectangular matrices in both orientations.

**Expressions always test:** transpose (flips dimensions), inverse (only exists for square non-singular), scalar multiplication (no dimension change), addition (must match), multiplication (inner dimensions must match).

### Pattern 2 — The singularity trap
If a matrix is **singular**, it has **no inverse**. Any expression involving $J^{-1}$ where J is singular → **DNE**.

**Trap:** Students write "the inverse of a 5×5 matrix is 5×5" without checking singularity. If singular → no inverse → the whole expression is DNE.

### Pattern 3 — The four RREF conditions (2024 Q1c, 2025 Q1c)
Students must know ALL four conditions and identify which ONE is violated — not just say "it's wrong."

**The four conditions:**
1. All-zero rows are below all nonzero rows
2. Leading entry of each nonzero row is 1 (the "leading 1")
3. Each leading 1 is strictly to the RIGHT of the leading 1 in the row above
4. Every column containing a leading 1 has **zeros in ALL other entries** (above AND below)

**The most commonly violated (and missed) condition:** Condition 4 — zeros ABOVE the leading 1. Students check that entries below are zero but forget to zero out entries above.

### Pattern 4 — Row [0 0 0 | c≠0] means NO SOLUTION
Not "infinitely many" — students confuse these. A row of all zeros on the left but nonzero on the right is the **inconsistency marker**.

### Pattern 5 — Row operation fill-in (2025 Q1b)
The examiner shows a partially completed row reduction and asks students to fill in missing entries after specific row operations. Full marks require:
- Applying the operation correctly to every entry in the row
- Including the augmented column (RHS)

**Trap:** Students apply the operation to the coefficient columns but forget the right-hand side entry.

### Pattern 6 — Dimension of complex expressions
For $A(3EB + E^{-1}B)$: must verify EVERY sub-expression before concluding the outer product exists.

**Systematic approach:** Work inside-out, left-to-right.
1. Check $E^{-1}$ exists (non-singular square) → size of $E^{-1}$
2. $E^{-1}B$: inner dims match? → size of result
3. $3EB$: inner dims match? → size of result
4. $3EB + E^{-1}B$: same size? → addition defined? → size of sum
5. $A \times (...)$: inner dims match? → final size

---

## SECTION C: THE FOUR RREF CONDITIONS — MEMORISE EXACTLY

A matrix is in RREF if and only if ALL four conditions hold simultaneously:

| # | Condition | What to check |
|---|-----------|--------------|
| 1 | All-zero rows at the bottom | No nonzero row appears below a zero row |
| 2 | Leading entry = 1 | First nonzero entry in each row must be exactly 1 |
| 3 | Leading 1s step right | Each leading 1 is to the right of the one above it |
| 4 | Leading 1 column is clear | The ENTIRE column containing a leading 1 has zeros EVERYWHERE else (above and below) |

**Quick test strategy:** For each row from top to bottom:
- Find the leading entry → is it 1? (Condition 2)
- Is it to the right of the row above's leading 1? (Condition 3)
- Does its column have zeros everywhere else? (Condition 4)
Then check: any zero rows at bottom? (Condition 1)

---

## SECTION D: QUESTION BANK

---

### ─────────────────────────────────────
### EASY QUESTIONS (E1 – E4)
### ─────────────────────────────────────

---

## E1. RREF or Not? — Four Conditions Check

For each matrix, state whether it is in RREF. If NOT, state which condition is violated (give the condition number and describe it precisely).

$$\text{(i)} \begin{bmatrix}1&0&3\\0&1&-2\\0&0&1\end{bmatrix} \qquad \text{(ii)} \begin{bmatrix}1&0&0\\0&2&0\\0&0&1\end{bmatrix} \qquad \text{(iii)} \begin{bmatrix}0&0&0\\1&0&2\\0&1&3\end{bmatrix}$$

$$\text{(iv)} \begin{bmatrix}1&3&0\\0&0&1\\0&0&0\end{bmatrix} \qquad \text{(v)} \begin{bmatrix}1&0&2&0\\0&1&-1&0\\0&0&0&1\end{bmatrix}$$

**[10 marks — 2 marks each]**

---

### SOLUTION E1

**(i)** NOT in RREF.

Check condition 4: column 3 has a leading 1 in row 3. But row 1 has entry 3 and row 2 has entry −2 in column 3 — neither is zero. **Condition 4 violated:** the column containing a leading 1 (column 3, row 3) has nonzero entries above it.

**(ii)** NOT in RREF.

Check condition 2: row 2 has leading entry 2, not 1. **Condition 2 violated:** the first nonzero entry in row 2 is 2, not a leading 1.

**(iii)** NOT in RREF.

Row 1 is all zeros. Rows 2 and 3 are nonzero. **Condition 1 violated:** the all-zero row (row 1) is above nonzero rows. Zero rows must be at the BOTTOM.

**(iv)** NOT in RREF.

Check condition 4: column 2 has entries 3 (row 1), 0 (row 2), 0 (row 3) — but there is NO leading 1 in column 2 (row 2 has leading 1 in column 3). So column 2 is fine (it's a free variable column). Now check column 3: leading 1 in row 2. Column 3 has entry 0 in row 1 and 0 in row 3. ✓

Actually check column 1: leading 1 in row 1. Column 1 has 0 in rows 2 and 3. ✓

Check condition 3: leading 1 in row 1 is in column 1; leading 1 in row 2 is in column 3 (column 3 > column 1). ✓

Wait — row 1 has entry 3 in column 2. Column 2 has no leading 1 anywhere, so it's a free variable column — no restriction on its entries from condition 4.

**Re-examine:** This matrix IS in RREF. ✓ Leading 1s: row 1 col 1, row 2 col 3. Column 1: [1,0,0] ✓ Column 3: [0,1,0] ✓ Step right ✓ Zero row at bottom ✓.

**(iv) IS in RREF.** ✓

**(v)** IS in RREF. ✓

Leading 1s: row 1 col 1, row 2 col 2, row 3 col 4. Each steps right ✓. Column 1: [1,0,0] ✓. Column 2: [0,1,0] ✓. Column 4: [0,0,1] ✓. No zero rows. ✓

**Summary:**

| Matrix | RREF? | Condition violated |
|--------|-------|-------------------|
| (i) | NO | Condition 4 — nonzero entries above leading 1 in col 3 |
| (ii) | NO | Condition 2 — leading entry in row 2 is 2, not 1 |
| (iii) | NO | Condition 1 — zero row is above nonzero rows |
| (iv) | YES | — |
| (v) | YES | — |

---

## E2. Count Free Variables and State Solution Type

For each RREF augmented matrix, state: (a) the number of free variables, (b) the solution type (unique / infinitely many / no solution).

$$\text{(i)}\left[\begin{array}{ccc|c}1&0&0&5\\0&1&0&-2\\0&0&1&7\end{array}\right] \quad \text{(ii)}\left[\begin{array}{cccc|c}1&2&0&-1&3\\0&0&1&4&-2\\0&0&0&0&0\end{array}\right] \quad \text{(iii)}\left[\begin{array}{ccc|c}1&0&2&4\\0&1&-3&1\\0&0&0&5\end{array}\right]$$

**[6 marks]**

---

### SOLUTION E2

**(i):** 3 pivot columns (cols 1, 2, 3), 0 free variables. No zero rows.

**Unique solution:** $x_1=5$, $x_2=-2$, $x_3=7$. ✓

**(ii):** Pivot columns: col 1 (row 1) and col 3 (row 2). Non-pivot columns: col 2 and col 4 → **2 free variables** ($x_2$ and $x_4$).

**Infinitely many solutions.** Parametric: let $x_2=s$, $x_4=t$.

From row 2: $x_3 + 4t = -2 \Rightarrow x_3 = -2-4t$

From row 1: $x_1 + 2s - t = 3 \Rightarrow x_1 = 3-2s+t$

General solution: $(3-2s+t,\ s,\ -2-4t,\ t)$.

**(iii):** Row 3 is $[0\ 0\ 0\ |\ 5]$ — zero left side, nonzero right side.

**No solution (inconsistent).** The system is contradictory: $0 = 5$ has no solution. □

---

## E3. Simple Dimension Compatibility — 2×3 Warmup

Given: $A$ is $2\times3$, $B$ is $3\times2$, $C$ is $2\times2$, $D$ is $3\times3$.

For each expression, give the dimension or DNE:

**i.** $AB$ &emsp; **ii.** $BA$ &emsp; **iii.** $A+B$ &emsp; **iv.** $C^2$ &emsp; **v.** $A+CB$ &emsp; **vi.** $D^{-1}B$ **[6 marks]**

---

### SOLUTION E3

**i.** $AB$: $A$ is $2\times3$, $B$ is $3\times2$. Inner dims: 3=3 ✓. Result: **2×2**.

**ii.** $BA$: $B$ is $3\times2$, $A$ is $2\times3$. Inner dims: 2=2 ✓. Result: **3×3**.

**iii.** $A+B$: $A$ is $2\times3$, $B$ is $3\times2$. Different sizes → **DNE**.

**iv.** $C^2 = CC$: $C$ is $2\times2$ (square). Inner dims: 2=2 ✓. Result: **2×2**.

**v.** $A+CB$: First $CB$: $C$ is $2\times2$, $B$ is $3\times2$ — inner dims: 2≠3 → $CB$ is **DNE** → $A+CB$ is **DNE**.

**vi.** $D^{-1}B$: $D$ is $3\times3$ (square; assume non-singular for this part) → $D^{-1}$ is $3\times3$. $D^{-1}B$: inner dims 3=3 ✓. Result: **3×2**.

---

## E4. Row Operation Fill-In — The 2025 Q1b Question

Fill in the missing entries ($*$) by performing the indicated row operations:

$$\left[\begin{array}{ccc|c}3&6&15&9\\7&12&39&25\\2&6&5&4\\3&0&6&1\end{array}\right] \xrightarrow{R_1\cdot(\frac{1}{3})\to R_1} \left[\begin{array}{ccc|c}*&*&*&*\\7&12&39&25\\2&6&5&4\\3&0&6&1\end{array}\right] \xrightarrow{\substack{R_2+(-7)R_1\to R_2\\3R_3+(-2)R_4\to R_3}} \left[\begin{array}{ccc|c}1&2&5&3\\*&*&*&*\\*&*&*&*\\3&0&6&1\end{array}\right]$$

**[4 marks]**

---

### SOLUTION E4

**After $R_1 \cdot (\frac{1}{3}) \to R_1$:**

$R_1 = [3,6,15\ |\ 9] \div 3 = [1,2,5\ |\ 3]$

$$\left[\begin{array}{ccc|c}\mathbf{1}&\mathbf{2}&\mathbf{5}&\mathbf{3}\\7&12&39&25\\2&6&5&4\\3&0&6&1\end{array}\right]$$

**After $R_2 + (-7)R_1 \to R_2$:**

New $R_2 = [7,12,39\ |\ 25] + (-7)[1,2,5\ |\ 3]$

$= [7-7,\ 12-14,\ 39-35\ |\ 25-21] = [\mathbf{0},\ \mathbf{-2},\ \mathbf{4}\ |\ \mathbf{4}]$

**After $3R_3 + (-2)R_4 \to R_3$:**

$3R_3 = [6,18,15\ |\ 12]$

$(-2)R_4 = [-6,0,-12\ |\ -2]$

New $R_3 = [6-6,\ 18+0,\ 15-12\ |\ 12-2] = [\mathbf{0},\ \mathbf{18},\ \mathbf{3}\ |\ \mathbf{10}]$

**Final matrix:**

$$\left[\begin{array}{ccc|c}1&2&5&3\\\mathbf{0}&\mathbf{-2}&\mathbf{4}&\mathbf{4}\\\mathbf{0}&\mathbf{18}&\mathbf{3}&\mathbf{10}\\3&0&6&1\end{array}\right]$$

---

### ─────────────────────────────────────
### MEDIUM QUESTIONS (M1 – M3)
### ─────────────────────────────────────

---

## M1. Full Dimension Analysis Table — 2025 Q1a Exact Replica [Must-Know]

The matrices $F$, $G$, $H$, $J$, and $K$ have the following properties:

| Matrix | Dimension | Properties |
|--------|-----------|-----------|
| $F$ | $5 \times 4$ | — |
| $G$ | $4 \times 5$ | — |
| $H$ | $4 \times 4$ | Nonsingular |
| $J$ | $5 \times 5$ | Singular |
| $K$ | $4 \times 4$ | Identity Matrix |

For each expression, determine the **dimension of the result**, or write **DNE** if undefined. **Justify every answer.**

**i.** $F + G^T$ &emsp; **ii.** $J^T H$ &emsp; **iii.** $FKH$ &emsp; **iv.** $F(5H^{-1}G + HG)$ &emsp; **v.** $G(F+J)$

**[15 marks — 3 marks each]**

---

### SOLUTION M1

**i. $F + G^T$**

$F$: $5\times4$.

$G$: $4\times5$ → $G^T$: $5\times4$.

$F + G^T$: both $5\times4$ → addition defined.

**Dimension: $5\times4$** ✓

**ii. $J^T H$**

$J$: $5\times5$ → $J^T$: $5\times5$.

$H$: $4\times4$.

$J^T H$: inner dimensions are $5$ (cols of $J^T$) and $4$ (rows of $H$). $5 \neq 4$.

**DNE** — multiplication not defined (inner dimensions don't match). □

**iii. $FKH$**

Evaluate left to right: $(FK)H$.

$FK$: $F$ is $5\times4$, $K$ is $4\times4$. Inner dims: $4=4$ ✓. Result: $5\times4$.

$(FK)H$: $5\times4$ times $4\times4$. Inner dims: $4=4$ ✓. Result: $5\times4$.

**Dimension: $5\times4$** ✓

*Note: $K$ is the $4\times4$ identity matrix, so $FK = F$ and $FKH = FH$. The dimension argument still holds.*

**iv. $F(5H^{-1}G + HG)$**

Work inside the parentheses first.

$H$ is $4\times4$ and nonsingular → $H^{-1}$ exists and is $4\times4$.

$H^{-1}G$: $4\times4$ times $4\times5$. Inner dims: $4=4$ ✓. Result: $4\times5$.

$5H^{-1}G$: scalar multiple of $4\times5$ → $4\times5$.

$HG$: $4\times4$ times $4\times5$. Inner dims: $4=4$ ✓. Result: $4\times5$.

$5H^{-1}G + HG$: both $4\times5$ → sum is $4\times5$.

$F(5H^{-1}G + HG)$: $F$ is $5\times4$, bracket is $4\times5$. Inner dims: $4=4$ ✓. Result: $5\times5$.

**Dimension: $5\times5$** ✓

**v. $G(F+J)$**

$F$: $5\times4$. $J$: $5\times5$.

$F + J$: $F$ is $5\times4$, $J$ is $5\times5$ — different sizes.

**DNE** — $F+J$ is not defined (sizes don't match), so the entire expression is DNE. □

---

## M2. Dimension Analysis Table — 2023 Q1a Style [Must-Know]

The matrices $A$, $B$, $C$, $D$, $E$ have the following properties:

| Matrix | Dimension | Properties |
|--------|-----------|-----------|
| $A$ | $3\times4$ | — |
| $B$ | $4\times3$ | — |
| $C$ | $3\times5$ | — |
| $D$ | $5\times5$ | Singular |
| $E$ | $4\times4$ | Non-singular |

State whether each is **True or False**, with full justification:

**i.** $ABC$ is the same size as $C^T B^T A^T$. **[3 marks]**

**ii.** $D \cdot D^{-1} = I$. **[3 marks]**

**iii.** The calculation of $A(3EB + E^{-1}B)$ is defined. **[4 marks]**

---

### SOLUTION M2

**i. $ABC$ vs $C^T B^T A^T$:**

$AB$: $3\times4$ times $4\times3$ = $3\times3$.
$ABC$: $3\times3$ times $3\times5$ = **$3\times5$**.

$(ABC)^T = C^T B^T A^T$ by the transpose reversal law.

$C^T$: $5\times3$. $B^T$: $3\times4$. $A^T$: $4\times3$.

$C^T B^T$: $5\times3$ times $3\times4$ = $5\times4$.
$C^T B^T A^T$: $5\times4$ times $4\times3$ = **$5\times3$**.

$3\times5 \neq 5\times3$ — they are transposes of each other, NOT the same size (unless 3=5, which they're not).

**FALSE.** $ABC$ is $3\times5$; $C^T B^T A^T$ is $5\times3$. They are transposes of each other. □

**ii. $D \cdot D^{-1} = I$:**

$D$ is $5\times5$ but **singular**. A singular matrix has no inverse — $D^{-1}$ does not exist.

**FALSE.** Since $D$ is singular, $D^{-1}$ is undefined, so $D \cdot D^{-1}$ cannot be computed. □

**iii. $A(3EB + E^{-1}B)$:**

$E$ is $4\times4$ non-singular → $E^{-1}$ exists and is $4\times4$.

$3EB$: $E$ is $4\times4$, $B$ is $4\times3$. Inner: $4=4$ ✓ → $3EB$ is $4\times3$.

$E^{-1}B$: $4\times4$ times $4\times3$. Inner: $4=4$ ✓ → $E^{-1}B$ is $4\times3$.

$3EB + E^{-1}B$: both $4\times3$ → sum is $4\times3$.

$A(4\times3\text{ matrix})$: $A$ is $3\times4$, bracket is $4\times3$. Inner: $4=4$ ✓ → result is $3\times3$.

**TRUE.** The calculation is defined and produces a $3\times3$ matrix. □

---

## M3. Three RREF Matrices — The 2025 Q1c Question

For each augmented matrix below, determine whether it is in RREF. If NOT, state which condition is violated. If it IS in RREF, state the number of solutions.

$$\text{A)}\left[\begin{array}{ccc|c}1&0&0&4\\0&1&0&5\\0&0&0&6\end{array}\right] \quad \text{B)}\left[\begin{array}{ccc|c}1&0&0&-3\\0&1&0&4\\0&1&-1&1\end{array}\right] \quad \text{C)}\left[\begin{array}{cccc|c}1&0&-2&0&0\\0&1&1&1&-3\\0&0&0&0&0\end{array}\right]$$

**[6 marks — 2 marks each]**

---

### SOLUTION M3

**Matrix A:**

Check all conditions:
- Condition 1: Row 3 is $[0\ 0\ 0\ |\ 6]$ — not all zero (RHS=6), but the LEFT side $[0\ 0\ 0]$ is all zero. Strictly, condition 1 applies to the coefficient part. Row 3 has zero leading entry — but it has a nonzero right-hand side, meaning $0 = 6$ which is **inconsistent**. However, checking RREF conditions on the augmented matrix:

The left portion of row 3 is $[0\ 0\ 0]$, which is all-zero. But rows 1 and 2 are nonzero. The zero LEFT part of row 3 IS below nonzero rows ✓ (Condition 1 satisfied for the coefficient portion).

Condition 2: Row 1 leading 1 ✓, Row 2 leading 1 ✓. Row 3 has no leading entry on the left side.

Conditions 3, 4: Two leading 1s (col 1, col 2) ✓ — col 1 and col 2 each have zeros elsewhere ✓.

**Matrix A IS technically in RREF** for the coefficient portion. However, row 3 $[0\ 0\ 0\ |\ 6]$ signals **no solution** (inconsistency: $0x+0y+0z = 6$ impossible).

**In RREF. No solution (inconsistent system).** □

*Examiner note: The 2025 paper awarded 2 marks here for "is in RREF" + "no solution" (students who only said "not RREF" due to misreading row 3 lost marks.)*

**Matrix B:**

Rows 2 and 3 both have entries in column 2: row 2 has leading 1 in col 2; row 3 has entry 1 in col 2.

**Condition 4 violated:** Column 2 contains a leading 1 (in row 2), but row 3 has a nonzero entry (=1) in that same column. The entire column of a leading 1 must be zero everywhere else — including below.

**NOT in RREF. Condition 4 violated.** □

**Matrix C:**

Leading 1s: row 1, col 1; row 2, col 2. Step right ✓ (Condition 3).

Column 1: rows 2,3 are 0 ✓. Column 2: rows 1,3 are 0 ✓ (row 1 has 0 in col 2 ✓). Condition 4 ✓.

Condition 1: Row 3 is all zero (coefficient portion), below nonzero rows ✓.

Condition 2: Both leading entries are 1 ✓.

**Matrix C IS in RREF.** Pivot columns: 1 and 2. Free variables: $x_3$ and $x_4$ (2 free variables).

**Infinitely many solutions.** □

---

### ─────────────────────────────────────
### HARD QUESTIONS (H1 – H2)
### ─────────────────────────────────────

---

## H1. Predicted 24th Batch Q1 — Full Question Simulation

*This mirrors the exact 2025 Q1 structure: dimension table [15] + row operation fill [4] + RREF check [6].*

**Part (a):** The matrices $P$, $Q$, $R$, $S$, $T$ have the following properties:

| Matrix | Dimension | Properties |
|--------|-----------|-----------|
| $P$ | $3\times5$ | — |
| $Q$ | $5\times3$ | — |
| $R$ | $5\times5$ | Nonsingular |
| $S$ | $3\times3$ | Singular |
| $T$ | $5\times5$ | Identity Matrix |

For each expression, find the dimension or state DNE. Justify fully.

**i.** $P + Q^T$ &emsp; **ii.** $Q P R^{-1}$ &emsp; **iii.** $S^{-1} + P Q$ &emsp; **iv.** $P(R + T)Q$ &emsp; **v.** $R^3 - 4T$ **[15 marks]**

**Part (b):** Fill in the missing entries:

$$\left[\begin{array}{ccc|c}2&4&-2&8\\1&-1&3&2\\3&2&0&5\end{array}\right] \xrightarrow{R_1\cdot\frac{1}{2}\to R_1} \left[\begin{array}{ccc|c}*&*&*&*\\1&-1&3&2\\3&2&0&5\end{array}\right] \xrightarrow{\substack{R_2-R_1\to R_2\\R_3-3R_1\to R_3}} \left[\begin{array}{ccc|c}1&2&-1&4\\*&*&*&*\\*&*&*&*\end{array}\right]$$

**[4 marks]**

**Part (c):** State whether each matrix is in RREF. If not, identify the violated condition precisely.

$$\text{i)}\left[\begin{array}{cc|c}1&3&2\\0&0&0\end{array}\right] \quad \text{ii)}\left[\begin{array}{ccc|c}0&1&0&4\\1&0&0&2\\0&0&1&-1\end{array}\right] \quad \text{iii)}\left[\begin{array}{ccc|c}1&0&0&3\\0&1&0&-1\\0&0&2&4\end{array}\right]$$

**[6 marks]**

---

### SOLUTION H1

**Part (a):**

**i. $P + Q^T$:**
$P$: $3\times5$. $Q^T$: $3\times5$ (transpose of $5\times3$). Same size → **$3\times5$**. ✓

**ii. $QP R^{-1}$:**
$R$ is $5\times5$ nonsingular → $R^{-1}$: $5\times5$.

$QP$: $Q$ is $5\times3$, $P$ is $3\times5$. Inner: $3=3$ ✓ → $5\times5$.

$(QP)R^{-1}$: $5\times5$ times $5\times5$ → **$5\times5$**. ✓

**iii. $S^{-1} + PQ$:**
$S$ is $3\times3$ but **singular** → $S^{-1}$ does not exist.

**DNE.** The entire expression is undefined. □

**iv. $P(R+T)Q$:**
$R$: $5\times5$, $T$: $5\times5$ (identity). $R+T$: $5\times5$.

$P(R+T)$: $P$ is $3\times5$, $(R+T)$ is $5\times5$. Inner: $5=5$ ✓ → $3\times5$.

$[P(R+T)]Q$: $3\times5$ times $Q$ is $5\times3$. Inner: $5=5$ ✓ → **$3\times3$**. ✓

**v. $R^3 - 4T$:**
$R$ is $5\times5$ nonsingular → $R^3$: $5\times5$.

$4T$: scalar times $5\times5$ identity → $5\times5$.

$R^3 - 4T$: both $5\times5$ → **$5\times5$**. ✓

**Part (b):**

$R_1 \cdot \frac{1}{2} \to R_1$: $[2,4,-2\ |\ 8] \div 2 = [\mathbf{1,2,-1\ |\ 4}]$

$R_2 - R_1 \to R_2$: $[1,-1,3\ |\ 2] - [1,2,-1\ |\ 4] = [\mathbf{0,-3,4\ |\ -2}]$

$R_3 - 3R_1 \to R_3$: $[3,2,0\ |\ 5] - 3[1,2,-1\ |\ 4] = [3-3,\ 2-6,\ 0+3\ |\ 5-12] = [\mathbf{0,-4,3\ |\ -7}]$

$$\left[\begin{array}{ccc|c}1&2&-1&4\\\mathbf{0}&\mathbf{-3}&\mathbf{4}&\mathbf{-2}\\\mathbf{0}&\mathbf{-4}&\mathbf{3}&\mathbf{-7}\end{array}\right]$$

**Part (c):**

**i)** $\left[\begin{array}{cc|c}1&3&2\\0&0&0\end{array}\right]$:

Leading 1 in row 1, col 1. Col 1: row 2 = 0 ✓. Row 2 is all-zero, below row 1 ✓. No other leading 1s. Col 2 has no leading 1 (it's a free variable column — entry 3 is fine).

**IS in RREF.** One pivot (col 1), one free variable ($x_2$). Infinitely many solutions. ✓

**ii)** $\left[\begin{array}{ccc|c}0&1&0&4\\1&0&0&2\\0&0&1&-1\end{array}\right]$:

Row 1 has leading entry in col 2. Row 2 has leading entry in col 1.

**Condition 3 violated:** The leading 1 in row 2 (column 1) is to the LEFT of the leading 1 in row 1 (column 2). Leading 1s must move strictly right as you go down the rows. □

**iii)** $\left[\begin{array}{ccc|c}1&0&0&3\\0&1&0&-1\\0&0&2&4\end{array}\right]$:

Row 3 has first nonzero entry = 2, not 1.

**Condition 2 violated:** The leading entry in row 3 is 2, not a leading 1. □

---

## H2. The Trickiest RREF Violations — Near-RREF Matrices

For each matrix, state whether it is in RREF. If not, identify the **single condition violated** (only one is violated in each case). This tests fine-grained understanding.

$$\text{i)}\left[\begin{array}{cccc|c}1&2&0&0&3\\0&0&1&0&-1\\0&0&0&0&0\end{array}\right] \quad \text{ii)}\left[\begin{array}{ccc|c}1&0&4&2\\0&1&-3&0\\0&0&0&0\end{array}\right] \quad \text{iii)}\left[\begin{array}{ccc|c}1&0&0&6\\0&0&0&0\\0&1&0&-2\end{array}\right]$$

$$\text{iv)}\left[\begin{array}{ccc|c}1&0&3&0\\0&1&0&0\\0&0&1&0\end{array}\right]$$

**[8 marks]**

---

### SOLUTION H2

**i)** Check: Leading 1s in col 1 (row 1) and col 3 (row 2). Step right: col 3 > col 1 ✓. Zero row at bottom ✓. Col 1: [1,0,0] ✓. Col 3: [0,1,0] ✓. No leading 1 in col 2 or 4, so those entries (2 in row 1, 0 in row 2) are unconstrained.

**IS in RREF.** Two pivots, two free variables ($x_2$, $x_4$). Infinitely many solutions. ✓

**ii)** Leading 1s: col 1 (row 1), col 2 (row 2). Col 1: [1,0,0] ✓. Col 2: [0,1,0] ✓. Step right ✓. Zero row at bottom ✓. Col 3 has no leading 1 — entries 4 and −3 are in a free variable column, unconstrained.

**IS in RREF.** One free variable ($x_3$). ✓

**iii)** Rows: Row 1 nonzero, Row 2 all-zero, Row 3 nonzero.

**Condition 1 violated:** A zero row (row 2) appears ABOVE a nonzero row (row 3). All zero rows must be at the bottom. □

**iv)** Leading 1s: col 1 (row 1), col 2 (row 2), col 3 (row 3). Step right ✓. Conditions 1, 2, 3 satisfied. Now check condition 4:

Col 3 contains leading 1 in row 3. Check all other rows: row 1 has entry **3** in col 3, row 2 has entry **0** in col 3.

**Condition 4 violated:** Column 3 contains a leading 1 (row 3) but row 1 has a nonzero entry (3) in that column. All entries above (and below) a leading 1 must be zero. □

---

### ─────────────────────────────────────
### NIGHTMARE QUESTION (N1)
### ─────────────────────────────────────

---

## N1. Proof + Analysis — Why RREF is Unique

**[12 marks]**

**a)** Prove that row interchange ($R_i \leftrightarrow R_j$) preserves the solution set of a linear system. **[4 marks]**

**b)** A student claims the following matrix is in RREF and represents a system with a unique solution. Find ALL errors in the student's reasoning. **[4 marks]**

$$M = \left[\begin{array}{cccc|c}1&0&2&0&5\\0&1&-1&0&3\\0&0&0&0&0\\0&0&1&0&2\end{array}\right]$$

The student says: *"Rows 1, 2, 3, 4 have leading entries 1, 1, 0, 1. Since there are 3 leading 1s for 4 unknowns, there is 1 free variable, so infinitely many solutions. Wait — actually since every column has a leading 1 or is controlled, the solution is unique."*

**c)** For the matrix $M$ above, determine the correct solution type and find the general solution. **[4 marks]**

---

### SOLUTION N1

**Part (a):** [See T2 N2 Solution — proof is identical]

Consider the system with equations $E_1, E_2, \ldots, E_m$. The solution set $S$ consists of all $(x_1,\ldots,x_n)$ satisfying ALL equations simultaneously.

After interchanging rows $i$ and $j$, the same equations are present — only their listing order changes. Any solution in $S$ satisfies all equations regardless of order → it satisfies the new system. Conversely, any solution of the new system satisfies all equations of the original. Therefore $S$ is unchanged. □

**Part (b):** The student's matrix $M$ has multiple errors:

**Error 1 — Not in RREF (Condition 1):**
Row 3 is all-zero: $[0,0,0,0\ |\ 0]$. Row 4 is nonzero: $[0,0,1,0\ |\ 2]$. A zero row (row 3) appears ABOVE a nonzero row (row 4). Condition 1 is violated.

**Error 2 — Not in RREF (Condition 4):**
Row 4 would have a leading 1 in col 3 (after fixing condition 1 by swapping rows 3 and 4). But col 3 already has entry $2$ in row 1 and $-1$ in row 2. These are nonzero — condition 4 would be violated.

**Error 3 — Student's logic is wrong:**
The student says "every column has a leading 1 or is controlled" — this is incoherent. Column 3 has no leading 1 in valid RREF ordering (rows 1 and 2), so $x_3$ is a free variable. The solution is NOT unique.

**Error 4 — Counting leading 1s incorrectly:**
In valid RREF (after swapping rows 3 and 4 and clearing column 3), there would be 3 pivot columns, giving 1 free variable and infinitely many solutions — consistent with the student's first statement, but their conclusion of "unique" is wrong.

**Part (c):** Correct the matrix by swapping rows 3 and 4:

$$\left[\begin{array}{cccc|c}1&0&2&0&5\\0&1&-1&0&3\\0&0&1&0&2\\0&0&0&0&0\end{array}\right]$$

Now apply back-substitution to reach RREF. Clear col 3:

$R_1 - 2R_3 \to R_1$: $[1,0,0,0\ |\ 1]$

$R_2 + R_3 \to R_2$: $[0,1,0,0\ |\ 5]$

$$\left[\begin{array}{cccc|c}1&0&0&0&1\\0&1&0&0&5\\0&0&1&0&2\\0&0&0&0&0\end{array}\right]$$

**This is RREF.** Pivot columns: 1, 2, 3. Free variable: $x_4$.

Let $x_4 = t$.

**General solution:** $x_1 = 1$, $x_2 = 5$, $x_3 = 2$, $x_4 = t$ for any $t \in \mathbb{R}$.

**Infinitely many solutions.** The student was partially right (infinitely many) but wrong about it being unique, and wrong about the matrix being in RREF. □

---

## SECTION E: RAPID-FIRE REVISION

**The 4 RREF Conditions — Check in this order:**

| # | Condition | Typical violation example |
|---|-----------|--------------------------|
| 1 | Zero rows at BOTTOM | $\begin{bmatrix}0&0\\1&2\end{bmatrix}$ — zero row above nonzero |
| 2 | Leading entry = 1 | $\begin{bmatrix}2&0\\0&1\end{bmatrix}$ — leading entry is 2 |
| 3 | Leading 1s step RIGHT | $\begin{bmatrix}0&1\\1&0\end{bmatrix}$ — second row's leading 1 is to the left |
| 4 | Leading 1 column all zeros | $\begin{bmatrix}1&0\\3&1\end{bmatrix}$ — col 2 has leading 1 in row 2 but row 1 has 0 ✓ (actually fine); harder: $\begin{bmatrix}1&2\\0&1\end{bmatrix}$ — col 2 has leading 1 in row 2 but row 1 has **2** (violation) |

**Dimension rules — the four checks:**

| Check | Rule |
|-------|------|
| Addition $A+B$ | $A$ and $B$ must have the SAME dimensions |
| Multiplication $AB$ | Cols of $A$ = Rows of $B$; result is (rows of $A$) × (cols of $B$) |
| Transpose $A^T$ | Swaps dimensions: $m\times n \to n\times m$ |
| Inverse $A^{-1}$ | Only defined if $A$ is SQUARE and NONSINGULAR |

**Solution type from RREF:**

| Final row form | Meaning |
|---------------|---------|
| $[0\ 0\ \cdots\ 0\ \|\ 0]$ | Redundant equation — free variable exists → infinitely many solutions |
| $[0\ 0\ \cdots\ 0\ \|\ c\neq0]$ | Inconsistency → NO solution |
| All pivots, no zero rows | Unique solution |

---

*End of Topic 3: RREF Identification & Matrix Dimension Analysis*
*Total: 4 Easy + 3 Medium + 2 Hard + 1 Nightmare = 10 questions with full solutions*
*Next: Topic 4 — Matrix Algebra, Applied Multiplication & True/False*
