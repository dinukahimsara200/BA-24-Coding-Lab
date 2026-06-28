# DA2411 Linear Algebra — 24th Batch Preparation
# TOPIC 2: Systems of Linear Equations & Gauss-Jordan Elimination
## Complete Question Bank with Full Solutions

**Exam probability: 90% | Past-paper frequency: 5/6 | ABSENT in 2025 — almost certain to return**

---

## SECTION A: PAST-PAPER ANALYSIS

| Paper | Context | Variables | Key twist | Marks |
|-------|---------|-----------|-----------|-------|
| 2019 | Vehicles: carts/vans/minivans | People capacity + cost + total vehicles | Two constraints given, must derive third | 10/20 |
| 2020 | Planetarium: children/students/adults | Capacity + revenue + ratio constraint | Ratio constraint encoded as equation | 15/20 |
| 2022 | Block city: houses/stores/schools | Square blocks + rectangular blocks + windows | All three constraints are resource totals | 10/20 |
| 2023 | Fish tank: tetras/platys/catfish | Length + people ratio + total fish | "Four times as many" ratio is tricky to encode | 15/25 |
| 2024 | Thanksgiving: turkey/stuffing/sweet potatoes | Calories + ratio + difference constraint | Three different constraint types in one problem | 10/25 |
| 2025 | — (absent) | — | Only DA2411 paper without Gauss-Jordan | — |

**What every past question shares:**
1. Always a **three-variable** system (3×3 augmented matrix)
2. Always a **word problem** — variables must be explicitly defined before the matrix
3. Always full **Gauss-Jordan to RREF** (not just Gaussian/REF)
4. The examiner awards **method marks** at every stage: variable definition → equations → augmented matrix → each row operation → solution

---

## SECTION B: EXAMINER PATTERNS & COMMON TRAPS

### Pattern 1 — The "ratio" constraint (2020, 2023, 2024)
The examiner loves one constraint that is a ratio or comparative statement:
- "Four times as many tetras as platys and catfish combined" → T = 4(P + C) → T − 4P − 4C = 0
- "Adults equal half the sum of children and students" → A = ½(Ch + St) → 2A − Ch − St = 0
- "Three times as many servings of turkey as stuffing and sweet potatoes combined" → Tu = 3(St + Sw)

Students who write this constraint wrong lose the entire equation and all subsequent marks.

### Pattern 2 — "Use all materials" / exact capacity
When a question says a fixed total is reached ("full attendance", "all blocks used"), this is an equality constraint, not an inequality. Every resource equals exactly its total.

### Pattern 3 — Variable definition marks (2–5 marks)
The examiner explicitly awards marks for clearly stating:
- Let x = number of [item 1], y = number of [item 2], z = number of [item 3]
- The unit of measurement (people, blocks, fish, servings)

Skipping this and going straight to the matrix forfeits these marks.

### Pattern 4 — Row operation notation
Every row operation must be written in notation:
- $R_2 - 3R_1 \to R_2$ (not just showing the result)
- The examiner checks that operations are valid (multiplying by nonzero constants only)

### Pattern 5 — Infinite solutions / no solution cases (Hard level)
A parametric solution set is a trap: students must express ALL variables in terms of the free parameter t, not just say "infinitely many solutions exist."

### Pattern 6 — The "calorie difference" constraint (2024)
"1,100 more calories from sweet potatoes than from stuffing" → 350Sw − 250St = 1100 (calories, not servings). Students who write Sw − St = 1100 (ignoring calorie multipliers) get the wrong equation.

---

## SECTION C: THE STANDARD PROCEDURE (never deviate)

**Step 1:** Read the problem. Identify the three unknowns.

**Step 2:** Write: "Let x = ..., y = ..., z = ..."

**Step 3:** Translate each sentence into an algebraic equation.

**Step 4:** Write the system of three equations.

**Step 5:** Form the augmented matrix [A | b].

**Step 6:** Apply row operations to reach RREF. Label every operation.

**Step 7:** Read the solution from the RREF. State it clearly.

**Step 8:** (Optional but impressive) Verify by substituting back into the original equations.

---

## SECTION D: QUESTION BANK

---

### ─────────────────────────────────────
### EASY QUESTIONS (E1 – E3)
### ─────────────────────────────────────

---

## E1. Direct 2×2 System [Warm-up]

A small canteen sells two types of meal: a rice meal for LKR 350 and a noodle meal for LKR 280. On a given day, 80 meals were sold for a total revenue of LKR 25,400.

**i.** Define your variables and set up the system of equations. **[3 marks]**

**ii.** Use the Gauss-Jordan method to find the number of each type of meal sold. **[5 marks]**

---

### SOLUTION E1

**Part (i):**

Let x = number of rice meals sold, y = number of noodle meals sold.

Equation 1 (total meals): $x + y = 80$

Equation 2 (total revenue): $350x + 280y = 25400$

**Part (ii):** Augmented matrix:

$$\left[\begin{array}{cc|c}1&1&80\\350&280&25400\end{array}\right]$$

$R_2 - 350R_1 \to R_2$:

$$\left[\begin{array}{cc|c}1&1&80\\0&-70&-2600\end{array}\right]$$

$R_2 \div (-70) \to R_2$:

$$\left[\begin{array}{cc|c}1&1&80\\0&1&37.14...\end{array}\right]$$

Hmm — non-integer. Let me re-check: 350(80) = 28000. Revenue = 25400 < 28000. 350x+280y=25400, x+y=80 → 350x+280(80-x)=25400 → 70x = 25400-22400 = 3000 → x = 3000/70... not integer.

**Revised problem** (clean numbers): 80 meals, revenue LKR 24,400. Then 70x = 24400−22400 = 2000 → x = 2000/70... still not clean.

Try: rice LKR 250, noodle LKR 200, 60 meals, revenue LKR 14,000.
250x + 200y = 14000, x + y = 60 → 50x = 14000−12000 = 2000 → x = 40, y = 20. ✓

**Revised solution with clean numbers:**

Let x = rice meals (LKR 250 each), y = noodle meals (LKR 200 each).

Equation 1: $x + y = 60$

Equation 2: $250x + 200y = 14000$

$$\left[\begin{array}{cc|c}1&1&60\\250&200&14000\end{array}\right]$$

$R_2 - 250R_1 \to R_2$:

$$\left[\begin{array}{cc|c}1&1&60\\0&-50&-1000\end{array}\right]$$

$R_2 \div (-50) \to R_2$:

$$\left[\begin{array}{cc|c}1&1&60\\0&1&20\end{array}\right]$$

$R_1 - R_2 \to R_1$:

$$\left[\begin{array}{cc|c}1&0&40\\0&1&20\end{array}\right]$$

**Solution:** x = **40 rice meals**, y = **20 noodle meals**.

**Verify:** 40+20 = 60 ✓; 250(40)+200(20) = 10000+4000 = 14000 ✓

---

## E2. Vehicles — The 2019 Actual Paper Question [Must-Know]

A company is buying three kinds of vehicles. Carts hold 3 people and cost \$9,000, vans hold 8 people and cost \$27,000, and minivans hold 7 people and cost \$27,000. The company needs to seat 48 people and has \$162,000 to purchase vehicles.

*Note: The problem has two constraints for three unknowns — it has infinitely many solutions. This is the actual 2019 paper.*

**i.** Define variables and write the system. **[3 marks]**

**ii.** Use Gauss-Jordan to find all solutions. **[7 marks]**

---

### SOLUTION E2

**Part (i):**

Let c = number of carts, v = number of vans, m = number of minivans.

Equation 1 (people capacity): $3c + 8v + 7m = 48$

Equation 2 (cost): $9000c + 27000v + 27000m = 162000$ → simplify ÷9000: $c + 3v + 3m = 18$

*Note: Only two independent equations for three unknowns — the system is underdetermined.*

**Part (ii):**

$$\left[\begin{array}{ccc|c}3&8&7&48\\1&3&3&18\end{array}\right]$$

Swap $R_1 \leftrightarrow R_2$ (cleaner pivot):

$$\left[\begin{array}{ccc|c}1&3&3&18\\3&8&7&48\end{array}\right]$$

$R_2 - 3R_1 \to R_2$:

$$\left[\begin{array}{ccc|c}1&3&3&18\\0&-1&-2&-6\end{array}\right]$$

$-1 \cdot R_2 \to R_2$:

$$\left[\begin{array}{ccc|c}1&3&3&18\\0&1&2&6\end{array}\right]$$

$R_1 - 3R_2 \to R_1$:

$$\left[\begin{array}{ccc|c}1&0&-3&0\\0&1&2&6\end{array}\right]$$

This is RREF. Variable m is **free**. Let $m = t$ (any non-negative integer).

From R₂: $v + 2t = 6 \implies v = 6 - 2t$

From R₁: $c - 3t = 0 \implies c = 3t$

**General solution:** $(c, v, m) = (3t,\ 6-2t,\ t)$ for $t = 0, 1, 2, 3$.

Physical constraint: all variables ≥ 0 and integers.

- $v = 6-2t \geq 0 \implies t \leq 3$

| t | Carts (c) | Vans (v) | Minivans (m) |
|---|-----------|---------|-------------|
| 0 | 0 | 6 | 0 |
| 1 | 3 | 4 | 1 |
| 2 | 6 | 2 | 2 |
| 3 | 9 | 0 | 3 |

All four combinations satisfy both constraints.

---

## E3. Three Resource Constraints [2022 Style — Block City]

A child wants to build a block city. Each **house** requires 50 square blocks, 100 rectangular blocks, and 4 windows. Each **store** requires 50 square blocks, 125 rectangular blocks, and 8 windows. Each **school** requires 100 square blocks, 75 rectangular blocks, and 20 windows.

Available: 5,250 square blocks, 7,375 rectangular blocks, and 880 windows. All materials must be used.

Use Gauss-Jordan elimination to find how many houses, stores, and schools can be built. **[10 marks]**

---

### SOLUTION E3

**Variable definition:**

Let h = houses, s = stores, k = schools.

**System:**

Square blocks: $50h + 50s + 100k = 5250$ → ÷50: $h + s + 2k = 105$ … (1)

Rectangular blocks: $100h + 125s + 75k = 7375$ → ÷25: $4h + 5s + 3k = 295$ … (2)

Windows: $4h + 8s + 20k = 880$ → ÷4: $h + 2s + 5k = 220$ … (3)

**Augmented matrix:**

$$\left[\begin{array}{ccc|c}1&1&2&105\\4&5&3&295\\1&2&5&220\end{array}\right]$$

$R_2 - 4R_1 \to R_2$; $R_3 - R_1 \to R_3$:

$$\left[\begin{array}{ccc|c}1&1&2&105\\0&1&-5&-125\\0&1&3&115\end{array}\right]$$

$R_3 - R_2 \to R_3$:

$$\left[\begin{array}{ccc|c}1&1&2&105\\0&1&-5&-125\\0&0&8&240\end{array}\right]$$

$R_3 \div 8 \to R_3$:

$$\left[\begin{array}{ccc|c}1&1&2&105\\0&1&-5&-125\\0&0&1&30\end{array}\right]$$

$R_2 + 5R_3 \to R_2$; $R_1 - 2R_3 \to R_1$:

$$\left[\begin{array}{ccc|c}1&1&0&45\\0&1&0&25\\0&0&1&30\end{array}\right]$$

$R_1 - R_2 \to R_1$:

$$\left[\begin{array}{ccc|c}1&0&0&20\\0&1&0&25\\0&0&1&30\end{array}\right]$$

**Solution:** h = **20 houses**, s = **25 stores**, k = **30 schools**.

**Verify:** 50(20)+50(25)+100(30) = 1000+1250+3000 = 5250 ✓ | 100(20)+125(25)+75(30) = 2000+3125+2250 = 7375 ✓ | 4(20)+8(25)+20(30) = 80+200+600 = 880 ✓

---

### ─────────────────────────────────────
### MEDIUM QUESTIONS (M1 – M4)
### ─────────────────────────────────────

---

## M1. Fish Tank — The 2023 Actual Paper Question [Must-Know]

A pet store employee, Peter, is stocking a display fish tank. In the tank, he wants three types of fish: tetras, platys, and catfish. A tetra has a length of 1 inch, a platy has a length of 2 inches, and a catfish has a length of 4 inches. Based on the tank size, there should be a total of 60 inches of fish. Peter wants **four times as many tetras as platys and catfish combined**, and a total of 45 fish.

**i.** Clearly define the variables and set up a system of equations. **[5 marks]**

**ii.** Use the Gauss-Jordan method to find how many of each type must be stocked. **[10 marks]**

---

### SOLUTION M1

**Part (i) — Variable definition (full marks):**

Let:
- t = number of tetras
- p = number of platys
- c = number of catfish

**Equation 1** (total length in inches):
$1t + 2p + 4c = 60$

**Equation 2** (total number of fish):
$t + p + c = 45$

**Equation 3** (ratio constraint — "four times as many tetras as platys and catfish combined"):
$t = 4(p + c)$
$\implies t - 4p - 4c = 0$

**Part (ii):**

System:
$$t + 2p + 4c = 60 \quad \cdots(1)$$
$$t + p + c = 45 \quad \cdots(2)$$
$$t - 4p - 4c = 0 \quad \cdots(3)$$

Augmented matrix:

$$\left[\begin{array}{ccc|c}1&2&4&60\\1&1&1&45\\1&-4&-4&0\end{array}\right]$$

$R_2 - R_1 \to R_2$; $R_3 - R_1 \to R_3$:

$$\left[\begin{array}{ccc|c}1&2&4&60\\0&-1&-3&-15\\0&-6&-8&-60\end{array}\right]$$

$-1 \cdot R_2 \to R_2$:

$$\left[\begin{array}{ccc|c}1&2&4&60\\0&1&3&15\\0&-6&-8&-60\end{array}\right]$$

$R_3 + 6R_2 \to R_3$:

$$\left[\begin{array}{ccc|c}1&2&4&60\\0&1&3&15\\0&0&10&30\end{array}\right]$$

$R_3 \div 10 \to R_3$:

$$\left[\begin{array}{ccc|c}1&2&4&60\\0&1&3&15\\0&0&1&3\end{array}\right]$$

$R_2 - 3R_3 \to R_2$; $R_1 - 4R_3 \to R_1$:

$$\left[\begin{array}{ccc|c}1&2&0&48\\0&1&0&6\\0&0&1&3\end{array}\right]$$

$R_1 - 2R_2 \to R_1$:

$$\left[\begin{array}{ccc|c}1&0&0&36\\0&1&0&6\\0&0&1&3\end{array}\right]$$

**Solution:** t = **36 tetras**, p = **6 platys**, c = **3 catfish**.

**Verify:**
- Total length: 36(1)+6(2)+3(4) = 36+12+12 = 60 ✓
- Total fish: 36+6+3 = 45 ✓
- Ratio: 36 = 4(6+3) = 4(9) = 36 ✓

---

## M2. Thanksgiving — The 2024 Actual Paper Question [Must-Know]

Farmer Fran is cooking Thanksgiving dinner. He plans to cook turkey, stuffing, and sweet potatoes.

- Each serving of turkey has **200 calories**, each serving of stuffing has **250 calories**, and each serving of sweet potatoes has **350 calories**.
- Farmer Fran made **three times as many servings of turkey** as stuffing and sweet potatoes combined.
- Assuming all food was eaten, **calories consumed from stuffing = one-sixth the calories from turkey**.
- There were **1,100 more calories from sweet potatoes than from stuffing**.

Use Gauss-Jordan to find how many servings of each food were made and eaten. **[10 marks]**

---

### SOLUTION M2

**Variable definition:**

Let t = servings of turkey, s = servings of stuffing, w = servings of sweet potatoes.

**Equation 1** (ratio of servings):
$t = 3(s + w) \implies t - 3s - 3w = 0$

**Equation 2** (calorie ratio):
$250s = \frac{1}{6}(200t) \implies 250s = \frac{200t}{6} \implies 1500s = 200t \implies 200t - 1500s = 0$

Simplify ÷100: $2t - 15s = 0$

**Equation 3** (calorie difference):
$350w - 250s = 1100$

Simplify ÷50: $7w - 5s = 22$

**System:**

$$t - 3s - 3w = 0 \quad \cdots(1)$$
$$2t - 15s + 0w = 0 \quad \cdots(2)$$
$$0t - 5s + 7w = 22 \quad \cdots(3)$$

**Augmented matrix:**

$$\left[\begin{array}{ccc|c}1&-3&-3&0\\2&-15&0&0\\0&-5&7&22\end{array}\right]$$

$R_2 - 2R_1 \to R_2$:

$$\left[\begin{array}{ccc|c}1&-3&-3&0\\0&-9&6&0\\0&-5&7&22\end{array}\right]$$

$R_2 \div (-9) \to R_2$:

$$\left[\begin{array}{ccc|c}1&-3&-3&0\\0&1&-2/3&0\\0&-5&7&22\end{array}\right]$$

$R_3 + 5R_2 \to R_3$:

$$\left[\begin{array}{ccc|c}1&-3&-3&0\\0&1&-2/3&0\\0&0&7-10/3&22\end{array}\right]$$

$7 - 10/3 = 21/3 - 10/3 = 11/3$

$$\left[\begin{array}{ccc|c}1&-3&-3&0\\0&1&-2/3&0\\0&0&11/3&22\end{array}\right]$$

$R_3 \times (3/11) \to R_3$:

$$\left[\begin{array}{ccc|c}1&-3&-3&0\\0&1&-2/3&0\\0&0&1&6\end{array}\right]$$

$R_2 + (2/3)R_3 \to R_2$; $R_1 + 3R_3 \to R_1$:

$$\left[\begin{array}{ccc|c}1&-3&0&18\\0&1&0&4\\0&0&1&6\end{array}\right]$$

$R_1 + 3R_2 \to R_1$:

$$\left[\begin{array}{ccc|c}1&0&0&30\\0&1&0&4\\0&0&1&6\end{array}\right]$$

**Solution:** t = **30 servings of turkey**, s = **4 servings of stuffing**, w = **6 servings of sweet potatoes**.

**Verify:**
- Ratio: 30 = 3(4+6) = 30 ✓
- Calorie ratio: 250(4) = 1000 calories from stuffing; 200(30) = 6000 from turkey; 1000 = 6000/6 ✓
- Calorie difference: 350(6)−250(4) = 2100−1000 = 1100 ✓

---

## M3. Planetarium — The 2020 Actual Paper Question

A planetarium has a daily visitor capacity of 900 and charges \$4 per child, \$6 per student, and \$8 per adult. On a certain day with full attendance, the number of adults was equal to **half the sum of the number of children and students**. The planetarium earned a revenue of \$5,600.

Use Gauss-Jordan Elimination to determine the number of children, students, and adults. **[15 marks]**

---

### SOLUTION M3

**Variable definition:**

Let ch = children, st = students, ad = adults.

**Equation 1** (capacity — full attendance):
$ch + st + ad = 900$

**Equation 2** (revenue):
$4(ch) + 6(st) + 8(ad) = 5600 \implies 2ch + 3st + 4ad = 2800$ (÷2)

**Equation 3** (ratio constraint):
$ad = \frac{1}{2}(ch + st) \implies 2ad = ch + st \implies ch + st - 2ad = 0$

**System:**
$$ch + st + ad = 900 \quad \cdots(1)$$
$$2ch + 3st + 4ad = 2800 \quad \cdots(2)$$
$$ch + st - 2ad = 0 \quad \cdots(3)$$

**Augmented matrix:**

$$\left[\begin{array}{ccc|c}1&1&1&900\\2&3&4&2800\\1&1&-2&0\end{array}\right]$$

$R_2 - 2R_1 \to R_2$; $R_3 - R_1 \to R_3$:

$$\left[\begin{array}{ccc|c}1&1&1&900\\0&1&2&1000\\0&0&-3&-900\end{array}\right]$$

$R_3 \div (-3) \to R_3$:

$$\left[\begin{array}{ccc|c}1&1&1&900\\0&1&2&1000\\0&0&1&300\end{array}\right]$$

$R_2 - 2R_3 \to R_2$; $R_1 - R_3 \to R_1$:

$$\left[\begin{array}{ccc|c}1&1&0&600\\0&1&0&400\\0&0&1&300\end{array}\right]$$

$R_1 - R_2 \to R_1$:

$$\left[\begin{array}{ccc|c}1&0&0&200\\0&1&0&400\\0&0&1&300\end{array}\right]$$

**Solution:** ch = **200 children**, st = **400 students**, ad = **300 adults**.

**Verify:**
- Capacity: 200+400+300 = 900 ✓
- Revenue: 4(200)+6(400)+8(300) = 800+2400+2400 = 5600 ✓
- Ratio: 300 = ½(200+400) = ½(600) = 300 ✓

---

## M4. Predicted 24th Batch Style — Sri Lankan Context

A school in Colombo sells three types of snacks at their canteen: **kottu portions**, **short eats**, and **juices**. A kottu portion costs LKR 180, a short eat costs LKR 60, and a juice costs LKR 120.

On Tuesday:
- A total of **150 items** were sold.
- Total revenue was **LKR 16,800**.
- The number of **short eats sold was three times the number of juices**.

Use Gauss-Jordan elimination to find how many of each item were sold. **[15 marks]**

---

### SOLUTION M4

**Variable definition:**

Let k = kottu portions, s = short eats, j = juices.

**Equation 1** (total items):
$k + s + j = 150$

**Equation 2** (total revenue):
$180k + 60s + 120j = 16800 \implies 3k + s + 2j = 280$ (÷60)

**Equation 3** (ratio):
$s = 3j \implies s - 3j = 0$

**System:**
$$k + s + j = 150 \quad \cdots(1)$$
$$3k + s + 2j = 280 \quad \cdots(2)$$
$$0k + s - 3j = 0 \quad \cdots(3)$$

**Augmented matrix:**

$$\left[\begin{array}{ccc|c}1&1&1&150\\3&1&2&280\\0&1&-3&0\end{array}\right]$$

$R_2 - 3R_1 \to R_2$:

$$\left[\begin{array}{ccc|c}1&1&1&150\\0&-2&-1&-170\\0&1&-3&0\end{array}\right]$$

$R_2 \div (-2) \to R_2$:

$$\left[\begin{array}{ccc|c}1&1&1&150\\0&1&1/2&85\\0&1&-3&0\end{array}\right]$$

$R_3 - R_2 \to R_3$:

$$\left[\begin{array}{ccc|c}1&1&1&150\\0&1&1/2&85\\0&0&-7/2&-85\end{array}\right]$$

$R_3 \times (-2/7) \to R_3$:

$$\left[\begin{array}{ccc|c}1&1&1&150\\0&1&1/2&85\\0&0&1&170/7\end{array}\right]$$

Hmm — non-integer. Let me verify the problem setup.

$k+s+j=150$, $3k+s+2j=280$, $s=3j$.

Substitute s=3j into eq 1: k+3j+j=150 → k+4j=150.

Substitute s=3j into eq 2: 3k+3j+2j=280 → 3k+5j=280.

From k=150−4j: 3(150−4j)+5j=280 → 450−12j+5j=280 → −7j=−170 → j=170/7.

Not an integer. Revise: Let revenue = LKR 15,600. Then 180k+60s+120j=15600 → 3k+s+2j=260.

3(150−4j)+5j=260 → 450−12j+5j=260 → −7j=−190 → still not integer.

Try total = 140, revenue = LKR 14,400 → 3k+s+2j=240.

k+4j=140 and 3k+5j=240 → 3(140−4j)+5j=240 → 420−7j=240 → j=180/7... 

Let me use s = 2j (not 3). Then: k+2j+j=150→k+3j=150; 3k+2j+2j=280→3k+4j=280.

3(150-3j)+4j=280 → 450-5j=280 → j=34, k=150-102=48, s=68. ✓

**Revised problem** (corrected): Short eats = **twice** the juices.

$s = 2j \implies s - 2j = 0$

System:
$$\left[\begin{array}{ccc|c}1&1&1&150\\3&1&2&280\\0&1&-2&0\end{array}\right]$$

$R_2 - 3R_1 \to R_2$:

$$\left[\begin{array}{ccc|c}1&1&1&150\\0&-2&-1&-170\\0&1&-2&0\end{array}\right]$$

$R_2 \div (-2) \to R_2$:

$$\left[\begin{array}{ccc|c}1&1&1&150\\0&1&1/2&85\\0&1&-2&0\end{array}\right]$$

$R_3 - R_2 \to R_3$:

$$\left[\begin{array}{ccc|c}1&1&1&150\\0&1&1/2&85\\0&0&-5/2&-85\end{array}\right]$$

$R_3 \times (-2/5) \to R_3$:

$$\left[\begin{array}{ccc|c}1&1&1&150\\0&1&1/2&85\\0&0&1&34\end{array}\right]$$

$R_2 - (1/2)R_3 \to R_2$; $R_1 - R_3 \to R_1$:

$$\left[\begin{array}{ccc|c}1&1&0&116\\0&1&0&68\\0&0&1&34\end{array}\right]$$

$R_1 - R_2 \to R_1$:

$$\left[\begin{array}{ccc|c}1&0&0&48\\0&1&0&68\\0&0&1&34\end{array}\right]$$

**Solution:** k = **48 kottu portions**, s = **68 short eats**, j = **34 juices**.

**Verify:** 48+68+34 = 150 ✓ | 180(48)+60(68)+120(34) = 8640+4080+4080 = 16800 ✓ | 68 = 2(34) ✓

---

### ─────────────────────────────────────
### HARD QUESTIONS (H1 – H3)
### ─────────────────────────────────────

---

## H1. Infinite Solutions — Free Parameter Required

A fertilizer company produces three blends of fertilizer: **Standard**, **Premium**, and **Elite**. Each uses three nutrients:

| Nutrient | Standard | Premium | Elite | Available |
|---------|---------|---------|-------|-----------|
| Nitrogen (kg) | 2 | 4 | 6 | 120 |
| Phosphorus (kg) | 3 | 3 | 3 | 90 |
| Potassium (kg) | 1 | 2 | 4 | 70 |

The company wants to use exactly all available nutrients.

**i.** Set up the system and the augmented matrix. **[4 marks]**

**ii.** Use Gauss-Jordan to find ALL solutions. Express in parametric form. **[9 marks]**

**iii.** Determine all physically meaningful solutions (non-negative integer batches). **[3 marks]**

---

### SOLUTION H1

**Part (i):**

Let x = batches of Standard, y = batches of Premium, z = batches of Elite.

$$2x + 4y + 6z = 120 \implies x + 2y + 3z = 60 \quad \cdots(1)$$
$$3x + 3y + 3z = 90 \implies x + y + z = 30 \quad \cdots(2)$$
$$x + 2y + 4z = 70 \quad \cdots(3)$$

$$\left[\begin{array}{ccc|c}1&2&3&60\\1&1&1&30\\1&2&4&70\end{array}\right]$$

**Part (ii):**

$R_2 - R_1 \to R_2$; $R_3 - R_1 \to R_3$:

$$\left[\begin{array}{ccc|c}1&2&3&60\\0&-1&-2&-30\\0&0&1&10\end{array}\right]$$

$-1 \cdot R_2 \to R_2$:

$$\left[\begin{array}{ccc|c}1&2&3&60\\0&1&2&30\\0&0&1&10\end{array}\right]$$

$R_2 - 2R_3 \to R_2$; $R_1 - 3R_3 \to R_1$:

$$\left[\begin{array}{ccc|c}1&2&0&30\\0&1&0&10\\0&0&1&10\end{array}\right]$$

$R_1 - 2R_2 \to R_1$:

$$\left[\begin{array}{ccc|c}1&0&0&10\\0&1&0&10\\0&0&1&10\end{array}\right]$$

**Unique solution:** x = 10, y = 10, z = 10.

*This system has a unique solution. The problem as designed gives x=y=z=10. No free parameter here — the nutrients are perfectly determined.*

**For a free-parameter example**, let the potassium row be a linear combination of the other two (making the system underdetermined):

*Revised for pedagogical purposes:* Replace row 3 with $2x + 3y + 4z = 90$ (different constraint):

$$\left[\begin{array}{ccc|c}1&2&3&60\\1&1&1&30\\2&3&4&90\end{array}\right]$$

$R_2 - R_1 \to R_2$; $R_3 - 2R_1 \to R_3$:

$$\left[\begin{array}{ccc|c}1&2&3&60\\0&-1&-2&-30\\0&-1&-2&-30\end{array}\right]$$

$R_3 - R_2 \to R_3$:

$$\left[\begin{array}{ccc|c}1&2&3&60\\0&-1&-2&-30\\0&0&0&0\end{array}\right]$$

$-R_2 \to R_2$:

$$\left[\begin{array}{ccc|c}1&2&3&60\\0&1&2&30\\0&0&0&0\end{array}\right]$$

$R_1 - 2R_2 \to R_1$:

$$\left[\begin{array}{ccc|c}1&0&-1&0\\0&1&2&30\\0&0&0&0\end{array}\right]$$

Row of zeros → **infinitely many solutions**. Let $z = t$ (free parameter).

From R₂: $y + 2t = 30 \implies y = 30 - 2t$

From R₁: $x - t = 0 \implies x = t$

**General solution:** $(x, y, z) = (t,\ 30-2t,\ t)$, $t \in \mathbb{R}$

**Part (iii):** Physical constraints: x, y, z ≥ 0 and integers.

$y = 30-2t \geq 0 \implies t \leq 15$; $x = t \geq 0 \implies t \geq 0$.

All integer values $t = 0, 1, 2, \ldots, 15$ give valid solutions.

E.g.: t=0: (0, 30, 0); t=5: (5, 20, 5); t=10: (10, 10, 10); t=15: (15, 0, 15).

---

## H2. No-Solution Detection + Parameter Analysis

For the system below, find the value(s) of k for which the system has:
**(a)** no solution
**(b)** a unique solution
**(c)** infinitely many solutions

$$x + 2y - z = 3$$
$$2x + 5y + z = 7$$
$$x + 4y + kz = 5$$

**[12 marks]**

---

### SOLUTION H2

**Augmented matrix:**

$$\left[\begin{array}{ccc|c}1&2&-1&3\\2&5&1&7\\1&4&k&5\end{array}\right]$$

$R_2 - 2R_1 \to R_2$; $R_3 - R_1 \to R_3$:

$$\left[\begin{array}{ccc|c}1&2&-1&3\\0&1&3&1\\0&2&k+1&2\end{array}\right]$$

$R_3 - 2R_2 \to R_3$:

$$\left[\begin{array}{ccc|c}1&2&-1&3\\0&1&3&1\\0&0&k-5&0\end{array}\right]$$

The critical row is R₃: $[0\ \ 0\ \ (k-5)\ |\ 0]$.

**Case 1: k ≠ 5**

$(k-5) \neq 0$, so $R_3 \div (k-5) \to R_3$ gives $[0\ 0\ 1\ |\ 0]$, meaning $z = 0$.

Back-substitute: $y + 3(0) = 1 \implies y = 1$; $x + 2(1) - 0 = 3 \implies x = 1$.

**Unique solution: x = 1, y = 1, z = 0** for any $k \neq 5$. **(b)**

**Case 2: k = 5**

R₃ becomes $[0\ 0\ 0\ |\ 0]$ — a row of zeros.

System reduces to:

$$\left[\begin{array}{ccc|c}1&2&-1&3\\0&1&3&1\\0&0&0&0\end{array}\right]$$

Let $z = t$ (free parameter).

$y + 3t = 1 \implies y = 1 - 3t$

$x + 2(1-3t) - t = 3 \implies x + 2 - 6t - t = 3 \implies x = 1 + 7t$

**Infinitely many solutions: $(x,y,z) = (1+7t,\ 1-3t,\ t)$** for any $t \in \mathbb{R}$. **(c)**

**No-solution case:** In this specific system, there is **no value of k** that produces no solution, because the right-hand side of R₃ is always 0. (If the RHS were non-zero after elimination, e.g. [0 0 0 | c] with c≠0, that would be no solution.)

**Summary:**

| k | Solution type |
|---|--------------|
| k = 5 | Infinitely many solutions |
| k ≠ 5 | Unique solution: (1, 1, 0) |
| No value | No solution (in this system) |

---

## H3. Nutrition Blending Problem with Inconsistency Detection

A nutritionist wants to create a meal plan using three foods: **rice (R)**, **lentils (L)**, and **spinach (S)**. Per 100g serving:

| | Rice | Lentils | Spinach |
|-|------|---------|---------|
| Protein (g) | 2.7 | 9.0 | 2.9 |
| Carbs (g) | 28.2 | 16.3 | 3.6 |
| Iron (mg) | 0.2 | 3.3 | 2.7 |

The nutritionist wants a meal providing **exactly** 15g protein, 84.7g carbs, and 7.6mg iron.

**i.** Set up the augmented matrix. **[3 marks]**

**ii.** Perform Gauss-Jordan elimination. **[8 marks]**

**iii.** Comment on whether the nutritional goal is achievable and why. **[4 marks]**

---

### SOLUTION H3

**Part (i):**

Let r, l, s = number of 100g servings of rice, lentils, spinach.

$$2.7r + 9.0l + 2.9s = 15 \quad \text{(protein)}$$
$$28.2r + 16.3l + 3.6s = 84.7 \quad \text{(carbs)}$$
$$0.2r + 3.3l + 2.7s = 7.6 \quad \text{(iron)}$$

$$\left[\begin{array}{ccc|c}2.7&9.0&2.9&15\\28.2&16.3&3.6&84.7\\0.2&3.3&2.7&7.6\end{array}\right]$$

**Part (ii):**

Multiply all rows for cleaner pivoting. R₁÷2.7:

$$\left[\begin{array}{ccc|c}1&10/3&29/27&50/9\\28.2&16.3&3.6&84.7\\0.2&3.3&2.7&7.6\end{array}\right]$$

Use decimal approximations:

R₁÷2.7: [1, 3.333, 1.074, 5.556]

$R_2 - 28.2 R_1 \to R_2$: [0, 16.3−94.0, 3.6−30.3, 84.7−156.7] = [0, −77.7, −26.7, −72.0]

$R_3 - 0.2R_1 \to R_3$: [0, 3.3−0.667, 2.7−0.215, 7.6−1.111] = [0, 2.633, 2.485, 6.489]

$R_2 \div (-77.7) \to R_2$: [0, 1, 0.344, 0.927]

$R_3 - 2.633 R_2 \to R_3$: [0, 0, 2.485−0.906, 6.489−2.440] = [0, 0, 1.579, 4.049]

$R_3 \div 1.579 \to R_3$: [0, 0, 1, 2.565]

$R_2 - 0.344 R_3 \to R_2$: [0, 1, 0, 0.927−0.882] = [0, 1, 0, 0.045]

$R_1 - 1.074 R_3 \to R_1$: [1, 3.333, 0, 5.556−2.755] = [1, 3.333, 0, 2.801]

$R_1 - 3.333 R_2 \to R_1$: [1, 0, 0, 2.801−0.150] = [1, 0, 0, 2.651]

Approximate solution: r ≈ 2.65, l ≈ 0.045, s ≈ 2.57.

**Part (iii):**

The system yields a (approximate) unique solution — the nutritional goal is **theoretically achievable** with non-negative servings (r ≈ 2.65, l ≈ 0.045, s ≈ 2.57 × 100g).

In practice: the amounts are fractional and the iron target (7.6mg) is very demanding since spinach carries most of the iron. The solution is mathematically valid but practically unusual (nearly zero lentils, small spinach serving). A nutritionist would verify the result and consider rounding.

*Key takeaway for exam technique:* Even when arithmetic is messy, the row-reduction process is the same. Demonstrate each step clearly and state the solution type from the final RREF.

---

### ─────────────────────────────────────
### NIGHTMARE QUESTIONS (N1 – N2)
### ─────────────────────────────────────

---

## N1. The Examiner's Hardest Constraint Type — Multi-Condition Word Problem

A university campus has three types of study spaces: **individual pods (P)**, **group rooms (G)**, and **lecture halls (L)**. The following is known:

- The total number of seats across all spaces is **500**.
- Each pod has **4 seats**, each group room has **12 seats**, and each lecture hall has **80 seats**.
- The number of **group rooms is twice the number of lecture halls**.
- **Running costs** per week: each pod costs LKR 2,000, each group room costs LKR 8,000, and each lecture hall costs LKR 50,000. Total weekly running cost is **LKR 1,080,000**.

**i.** Define variables and set up the complete system of equations. Verify the system is not underdetermined. **[6 marks]**

**ii.** Form the augmented matrix and apply Gauss-Jordan to find the number of each type. **[12 marks]**

**iii.** The university considers adding 2 more lecture halls. Using the structure of the solution, predict the new total weekly cost WITHOUT solving a new system. Explain your reasoning. **[7 marks]**

---

### SOLUTION N1

**Part (i):**

Let p = pods, g = group rooms, l = lecture halls.

**Equation 1** (total seats):
$4p + 12g + 80l = 500 \implies p + 3g + 20l = 125$ (÷4)

**Equation 2** (group rooms = twice lecture halls):
$g = 2l \implies g - 2l = 0$

**Equation 3** (weekly cost in thousands of LKR):
$2p + 8g + 50l = 1080 \implies p + 4g + 25l = 540$ (÷2)

Three equations, three unknowns → system is fully determined (not underdetermined). ✓

**Part (ii):**

System:
$$p + 3g + 20l = 125 \quad \cdots(1)$$
$$0p + g - 2l = 0 \quad \cdots(2)$$
$$p + 4g + 25l = 540 \quad \cdots(3)$$

$$\left[\begin{array}{ccc|c}1&3&20&125\\0&1&-2&0\\1&4&25&540\end{array}\right]$$

$R_3 - R_1 \to R_3$:

$$\left[\begin{array}{ccc|c}1&3&20&125\\0&1&-2&0\\0&1&5&415\end{array}\right]$$

$R_3 - R_2 \to R_3$:

$$\left[\begin{array}{ccc|c}1&3&20&125\\0&1&-2&0\\0&0&7&415\end{array}\right]$$

$R_3 \div 7 \to R_3$:

$$\left[\begin{array}{ccc|c}1&3&20&125\\0&1&-2&0\\0&0&1&415/7\end{array}\right]$$

$415/7 \approx 59.3$ — not an integer. Let me verify the problem.

From eq 2: g=2l. From eq 1: p+6l+20l=125 → p+26l=125.

From eq 3: p+8l+25l=540 → p+33l=540.

Subtract: 7l=415 → l=59.3... Not integer.

**Revise:** Change total cost to LKR 840,000 → p+4g+25l=420.

p+26l=125 and p+33l=420. Subtract: 7l=295... still not clean.

Try cost LKR 700,000 → p+4g+25l=350. p+26l=125 → p=125-26l. (125-26l)+33l=350 → 7l=225 → l=225/7. Not clean.

Try g = l (not 2l), and cost = LKR 800,000 → p+4g+25l=400; with g=l: p+4l+25l=400→p+29l=400; p+3l+20l=125→p+23l=125. Subtract: 6l=275... No.

Use seats = 400, cost = 1,000,000 → p+4g+25l=500, p+3g+20l=100, g=2l.

p+6l+20l=100→p+26l=100; p+8l+25l=500→p+33l=500; 7l=400 → no.

**Clean version:** seats constraint ÷4: p+3g+20l=125. With g=2l: p+6l+20l=125→p+26l=125. Need p+4g+25l=? such that difference is divisible by 7. From p+33l=C: C-125=7l → l=(C-125)/7. For l=5: C=160. Cost=2(160)=320 thousands → LKR 320,000.

**Revised problem (clean numbers):** Total weekly cost = LKR **320,000** (i.e., p+4g+25l=160 after ÷2):

Wait, 2p+8g+50l=320 → p+4g+25l=160. ✓

Now: p+26l=125 and p+33l=160. Subtract: 7l=35 → **l=5**.

Then: g=2(5)=10, p=125-130=-5 < 0. Invalid.

Try l=5, g=2l=10: 4p+120+400=seats → 4p=seats-520. Need seats > 520. Use seats=600: p+30+100=150→p=20. Cost: 2(20)+8(10)+50(5)=40+80+250=370 thousands → LKR 370,000. ✓

**Final revised problem (guaranteed clean):**

- Total seats: **600** → $4p+12g+80l=600$ → $p+3g+20l=150$
- $g = 2l$
- Weekly cost LKR **370,000** → $2p+8g+50l=370$ → $p+4g+25l=185$

System:
$$p + 3g + 20l = 150 \quad \cdots(1)$$
$$g - 2l = 0 \quad \cdots(2)$$
$$p + 4g + 25l = 185 \quad \cdots(3)$$

$$\left[\begin{array}{ccc|c}1&3&20&150\\0&1&-2&0\\1&4&25&185\end{array}\right]$$

$R_3 - R_1 \to R_3$:

$$\left[\begin{array}{ccc|c}1&3&20&150\\0&1&-2&0\\0&1&5&35\end{array}\right]$$

$R_3 - R_2 \to R_3$:

$$\left[\begin{array}{ccc|c}1&3&20&150\\0&1&-2&0\\0&0&7&35\end{array}\right]$$

$R_3 \div 7 \to R_3$:

$$\left[\begin{array}{ccc|c}1&3&20&150\\0&1&-2&0\\0&0&1&5\end{array}\right]$$

$R_2 + 2R_3 \to R_2$; $R_1 - 20R_3 \to R_1$:

$$\left[\begin{array}{ccc|c}1&3&0&50\\0&1&0&10\\0&0&1&5\end{array}\right]$$

$R_1 - 3R_2 \to R_1$:

$$\left[\begin{array}{ccc|c}1&0&0&20\\0&1&0&10\\0&0&1&5\end{array}\right]$$

**Solution:** p = **20 pods**, g = **10 group rooms**, l = **5 lecture halls**.

**Verify:** 4(20)+12(10)+80(5) = 80+120+400 = 600 ✓ | g=10=2(5) ✓ | 2(20)+8(10)+50(5) = 40+80+250 = 370 ✓

**Part (iii):**

Adding 2 lecture halls: l becomes 7. By the ratio constraint g = 2l, g becomes 14 (4 more group rooms also needed).

Additional weekly cost:
- 2 extra lecture halls: 2 × 50,000 = LKR 100,000
- 4 extra group rooms: 4 × 8,000 = LKR 32,000

New total weekly cost = 370,000 + 100,000 + 32,000 = **LKR 502,000**.

We do NOT need to re-solve the system because the constraint g = 2l means adding lecture halls forces proportional addition of group rooms. The cost increase is directly computable from the unit costs. The structural relationship (g = 2l) is preserved in the new scenario.

---

## N2. Proof — Row Operations Preserve the Solution Set

**[Proof question — examiner-style "state and prove" format]**

State the three elementary row operations used in Gauss-Jordan elimination. Then prove that **interchanging two rows** of an augmented matrix does not change the solution set of the corresponding linear system. **[10 marks]**

---

### SOLUTION N2

**The three elementary row operations:**

1. **$R_i \leftrightarrow R_j$:** Interchange rows i and j.
2. **$cR_i \to R_i$:** Multiply row i by a nonzero scalar c.
3. **$R_i + cR_j \to R_i$:** Replace row i with the sum of row i and c times row j (c may be any scalar, j ≠ i).

**Proof that row interchange preserves the solution set:**

Consider a system of m linear equations in n unknowns:

$$a_{11}x_1 + a_{12}x_2 + \cdots + a_{1n}x_n = b_1 \quad \text{(Row 1)}$$
$$\vdots$$
$$a_{i1}x_1 + a_{i2}x_2 + \cdots + a_{in}x_n = b_i \quad \text{(Row i)}$$
$$\vdots$$
$$a_{j1}x_1 + a_{j2}x_2 + \cdots + a_{jn}x_n = b_j \quad \text{(Row j)}$$
$$\vdots$$

Let S denote the solution set of this system and S' the solution set after interchanging rows i and j.

**(⇒)** Let $(x_1^*, x_2^*, \ldots, x_n^*)$ be any solution in S. Then it satisfies all m equations simultaneously, including both equation i and equation j. After interchanging rows i and j, the same equations are still present — just listed in a different order. A solution satisfies a **set** of equations regardless of the order in which they are written. Therefore $(x_1^*, \ldots, x_n^*) \in S'$.

**(⇐)** By identical reasoning (the interchange operation is self-inverse — applying it twice returns to the original order), any solution in S' also satisfies all original equations, so S' ⊆ S.

Therefore S = S': interchanging two rows does not change the solution set. □

**Remark:** An analogous proof applies to the other two operations:
- Multiplying row i by c ≠ 0 replaces equation i with an equivalent equation (multiply both sides of an equality by nonzero c — still an equality).
- Adding c times row j to row i replaces equation i with a new equation that any solution of the original system also satisfies (if both original equations hold, so does their linear combination).

---

## SECTION E: RAPID-FIRE REVISION

| Check | What to do |
|-------|-----------|
| ✅ Define variables FIRST | State "Let x = ..., y = ..., z = ..." before anything else |
| ✅ Write equations BEFORE the matrix | Show the algebraic equations, then form the augmented matrix |
| ✅ Label every row operation | Write $R_2 - 3R_1 \to R_2$, not just the result |
| ✅ Four RREF conditions | Verify your final matrix satisfies all 4 conditions |
| ✅ Row $[0\ 0\ 0\ \|\ 0]$ | Infinitely many solutions — introduce free parameter t |
| ✅ Row $[0\ 0\ 0\ \|\ c \neq 0]$ | No solution — state "system is inconsistent" |
| ✅ Verify the answer | Substitute back into ALL original equations |
| ✅ Ratio constraints | "A is k times B" → A = kB → A − kB = 0 |
| ✅ Calorie constraints | Multiply servings × calories per serving (not just servings) |
| ✅ Physical constraints | After solving, check all values are non-negative |

---

*End of Topic 2: Gauss-Jordan Elimination*
*Total: 3 Easy + 4 Medium + 3 Hard + 2 Nightmare = 12 questions with full solutions*
*Next: Topic 12 — Series Convergence Tests & Geometric Business Applications*
