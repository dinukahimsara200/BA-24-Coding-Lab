# DA2411 Linear Algebra — 24th Batch Preparation
# TOPIC 12: Infinite Series & Convergence Tests
## Complete Question Bank with Full Solutions

**Exam probability: 90% | Past-paper frequency: 3/3 DA2411 papers | Always in Q4 | 10–15 marks per paper**

---

## SECTION A: PAST-PAPER ANALYSIS

| Paper | Series questions | Tests used | Marks |
|-------|-----------------|------------|-------|
| 2023 (21 Batch) | (i) Σ n/(n+5) — Divergence Test; (ii) Σ 1/(n² ln n) — Comparison Test; (iii) Geometric business: company profit decreasing 12%/yr | Divergence, Comparison, Geometric | 15/25 |
| 2024 (22 Batch) | Full Q4: Taylor series + R + interval + approximate ln(25) | Ratio Test for R, AST + p-series at endpoints | 25/25 |
| 2025 (23 Batch) | (d) Geometric series — paint layers; (e) Σ 1/(n ln n) — Integral Test | Geometric sum formula, Integral Test | 10/25 |

**The pattern across all three DA2411 papers:**
1. **One geometric series business application** (5 marks) — appears in 2/3 papers, very likely to recur
2. **One or two convergence/divergence determination** items (5 marks each) — appears in every paper
3. The tests rotate: Divergence (2023), Comparison (2023), Integral (2025) — **Ratio Test and Alternating Series Test have NOT yet appeared as standalone items in DA2411** → high probability of appearing in 2026

---

## SECTION B: EXAMINER PATTERNS & COMMON TRAPS

### Pattern 1 — Geometric Business Application (2023 Q4a, 2025 Q4d)
Always structured as: first term a, common ratio r = (1 ± k%), find total sum.
The examiner expects:
1. Identify a and r explicitly
2. Check |r| < 1 (justify convergence)
3. Apply S = a/(1−r)
4. Interpret in context (total profit, total paint, etc.)

**Trap:** Writing r = 1.12 instead of r = 0.88 for "decreases by 12%." A decrease means each term is SMALLER, so r < 1.

### Pattern 2 — Divergence Test (2023 Q4c-i)
Always try this first. If lim aₙ ≠ 0, the series diverges — done, no further work needed.

**Trap:** Students apply the Ratio Test or Comparison Test when lim aₙ = n/(n+5) → 1 ≠ 0 is immediately obvious. This wastes time and risks errors. The Divergence Test is the "first check" rule.

### Pattern 3 — Integral Test with ln (2025 Q4e, echoing 2023 Q4c-ii)
The examiner loves series involving ln n in the denominator:
- Σ 1/(n ln n): Integral Test → ∫ dx/(x ln x) = ln(ln x) → ∞ → **diverges**
- Σ 1/(n² ln n): Comparison Test → 1/(n² ln n) < 1/n² → Σ 1/n² converges (p=2) → **converges**

**Trap:** Students try the p-Series Test on Σ 1/(n ln n) and say "p = 1, diverges." Wrong — this is NOT a p-series (ln n is not a power of n). Must use Integral Test.

### Pattern 4 — Choosing the right test
The examiner expects you to STATE which test you are using BEFORE applying it. Writing the test name earns a method mark even if the algebra has errors.

### Pattern 5 — Ratio Test for factorials
When aₙ involves n! or kⁿ, use the Ratio Test. The cancellation makes it elegant.

**Trap:** After getting L < 1 from the Ratio Test, students write "converges" without checking if this is absolute or conditional convergence. For the DA2411 level, stating "converges absolutely" after L < 1 is the full answer.

### Pattern 6 — Alternating Series Test conditions
Two conditions must BOTH be checked:
1. bₙ₊₁ ≤ bₙ (non-increasing)
2. lim bₙ = 0

**Trap:** Students check only condition 2 and forget condition 1. If bₙ is not monotonically decreasing, the AST does not apply even if bₙ → 0.

---

## SECTION C: TEST SELECTION GUIDE

| Look at the series | Use this test |
|-------------------|--------------|
| aₙ → nonzero constant | **Divergence Test** (instant divergence) |
| Σ arⁿ form | **Geometric Series** (find a and r, check \|r\| < 1) |
| Σ 1/nᵖ form | **p-Series** (converges iff p > 1) |
| (-1)ⁿ bₙ with bₙ > 0 | **Alternating Series Test** (check bₙ decreasing AND → 0) |
| Contains n! or kⁿ | **Ratio Test** (best cancellation) |
| Of the form (bₙ)ⁿ | **Root Test** |
| Looks like 1/nᵖ but with extra factor (ln n, etc.) | **Comparison Test** or **Integral Test** |
| f(n) easy to integrate | **Integral Test** |
| Σ 1/(n ln n) specifically | **Integral Test** → diverges |
| Σ 1/(n² ln n) specifically | **Comparison** with 1/n² → converges |

---

## SECTION D: QUESTION BANK

---

### ─────────────────────────────────────
### EASY QUESTIONS (E1 – E4)
### ─────────────────────────────────────

---

## E1. Geometric Series — Sum Formula [Foundation]

Find the sum of the following geometric series, or state that it diverges:

**a)** $\displaystyle\sum_{n=1}^{\infty} \frac{5}{3^{n-1}}$ **[3 marks]**

**b)** $\displaystyle 6 - 4 + \frac{8}{3} - \frac{16}{9} + \cdots$ **[3 marks]**

**c)** $\displaystyle\sum_{n=0}^{\infty} \left(\frac{7}{5}\right)^n$ **[2 marks]**

---

### SOLUTION E1

**Part (a):**

Identify: $a = 5$, $r = \frac{1}{3}$ (ratio between successive terms).

Since $|r| = \frac{1}{3} < 1$, the series **converges**.

$$S = \frac{a}{1-r} = \frac{5}{1 - \frac{1}{3}} = \frac{5}{\frac{2}{3}} = \boxed{\frac{15}{2} = 7.5}$$

**Part (b):**

Identify: $a = 6$, $r = \frac{-4}{6} = -\frac{2}{3}$.

Verify: $6 \times (-\frac{2}{3}) = -4$ ✓; $(-4) \times (-\frac{2}{3}) = \frac{8}{3}$ ✓

Since $|r| = \frac{2}{3} < 1$, the series **converges**.

$$S = \frac{6}{1-(-\frac{2}{3})} = \frac{6}{\frac{5}{3}} = \frac{18}{5} = \boxed{3.6}$$

**Part (c):**

$r = \frac{7}{5} = 1.4 > 1$, so $|r| \geq 1$. The series **diverges**.

---

## E2. Divergence Test — Instant Decisions [2023 Q4c-i style]

For each series, determine convergence or divergence. If the Divergence Test applies, state it explicitly.

**a)** $\displaystyle\sum_{n=1}^{\infty} \frac{n}{n+5}$ **[3 marks]**

**b)** $\displaystyle\sum_{n=1}^{\infty} \frac{3n^2+1}{n^2+4}$ **[3 marks]**

**c)** $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^2+1}$ **[2 marks]**

---

### SOLUTION E2

**Part (a):** [This is the exact 2023 Q4c-i question]

Compute $\lim_{n\to\infty} \frac{n}{n+5}$. Divide numerator and denominator by $n$:

$$\lim_{n\to\infty} \frac{1}{1 + \frac{5}{n}} = \frac{1}{1+0} = 1 \neq 0$$

By the **Divergence Test** (Test for Divergence): since $\lim_{n\to\infty} a_n = 1 \neq 0$, the series $\displaystyle\sum_{n=1}^{\infty} \frac{n}{n+5}$ **diverges**. □

**Part (b):**

$$\lim_{n\to\infty} \frac{3n^2+1}{n^2+4} = \lim_{n\to\infty} \frac{3 + \frac{1}{n^2}}{1 + \frac{4}{n^2}} = \frac{3}{1} = 3 \neq 0$$

By the **Divergence Test**: the series **diverges**. □

**Part (c):**

$$\lim_{n\to\infty} \frac{1}{n^2+1} = 0$$

The Divergence Test is **inconclusive** (lim = 0 does not guarantee convergence). We need another test.

Since $\frac{1}{n^2+1} < \frac{1}{n^2}$ and $\sum \frac{1}{n^2}$ converges (p-series, p=2 > 1), by the **Comparison Test** the series **converges**. □

---

## E3. p-Series Classification

State whether each series converges or diverges, citing the p-Series Test:

**a)** $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n^3}$ &emsp; **b)** $\displaystyle\sum_{n=1}^{\infty} \frac{1}{\sqrt{n}}$ &emsp; **c)** $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n}$ &emsp; **d)** $\displaystyle\sum_{n=1}^{\infty} n^{-4/3}$

**[6 marks]**

---

### SOLUTION E3

Each series has form $\sum 1/n^p$.

**a)** $p = 3 > 1$ → **converges** ✓

**b)** $\sum 1/\sqrt{n} = \sum n^{-1/2}$, $p = \frac{1}{2} \leq 1$ → **diverges** ✓

**c)** Harmonic series: $p = 1 \leq 1$ → **diverges** ✓

**d)** $p = \frac{4}{3} > 1$ → **converges** ✓

**Summary table:**

| Series | p | Conclusion |
|--------|---|-----------|
| $\sum 1/n^3$ | 3 | Converges |
| $\sum 1/\sqrt{n}$ | 1/2 | Diverges |
| $\sum 1/n$ | 1 | Diverges |
| $\sum n^{-4/3}$ | 4/3 | Converges |

---

## E4. Geometric Series Business Application — The 2023 Paper Question [Must-Know]

A company had a profit of **\$35,000 in its first year**. Since then the company's profit has **decreased by 12% per year**. Assuming this trend continues, what is the **total profit the company can make over the course of its lifetime**? **[5 marks]**

---

### SOLUTION E4

**Identify the geometric series:**

Year 1 profit: $a = 35{,}000$

Each year profit decreases by 12%, so each year's profit is 88% of the previous year's:

$$r = 1 - 0.12 = 0.88$$

The profits form a geometric series: $35000 + 35000(0.88) + 35000(0.88)^2 + \cdots$

**Check convergence:**

$|r| = 0.88 < 1$ → the series **converges** ✓

*(Economically: profits shrink toward zero over time, so total lifetime profit is finite.)*

**Compute the sum:**

$$S = \frac{a}{1-r} = \frac{35{,}000}{1 - 0.88} = \frac{35{,}000}{0.12} = \boxed{\$291{,}666.67}$$

**Interpretation:** Over its entire lifetime, the company will earn a total of approximately **\$291,667** in profit.

---

### ─────────────────────────────────────
### MEDIUM QUESTIONS (M1 – M5)
### ─────────────────────────────────────

---

## M1. Integral Test — The Examiner's Favourite Hard Case [2025 Q4e exact]

Determine whether the following series converges or diverges:

$$\sum_{n=2}^{\infty} \frac{1}{n \ln n}$$

**[5 marks]**

---

### SOLUTION M1

**Test selection:** The general term is $a_n = \frac{1}{n \ln n}$. This is NOT a p-series (ln n is not a power of n). The function $f(x) = \frac{1}{x \ln x}$ is positive, continuous, and decreasing on $[2, \infty)$, so we apply the **Integral Test**.

**Evaluate $\displaystyle\int_2^{\infty} \frac{1}{x \ln x}\,dx$:**

Use substitution $u = \ln x$, $du = \frac{1}{x}dx$:

$$\int_2^{\infty} \frac{1}{x \ln x}\,dx = \int_{\ln 2}^{\infty} \frac{1}{u}\,du = \Big[\ln u\Big]_{\ln 2}^{\infty} = \lim_{t\to\infty}\ln t - \ln(\ln 2) = \infty$$

The integral **diverges**.

**Conclusion:** By the **Integral Test**, since $\displaystyle\int_2^{\infty}\frac{1}{x\ln x}\,dx$ diverges, the series $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n\ln n}$ **diverges**. □

**Examiner note:** The 2025 paper asked this exact question for 5 marks. The substitution step is where marks are earned — show it explicitly.

---

## M2. Comparison Test — The 2023 Q4c-ii Question [Must-Know]

Determine whether the following series converges or diverges:

$$\sum_{n=2}^{\infty} \frac{1}{n^2 \ln n}$$

**[5 marks]**

---

### SOLUTION M2

**Test selection:** The general term $\frac{1}{n^2 \ln n}$ resembles $\frac{1}{n^2}$ but is smaller (since $\ln n > 1$ for $n \geq 3$). This suggests the **Comparison Test**.

**Establish the comparison:**

For $n \geq 3$: $\ln n > 1$, so:

$$\frac{1}{n^2 \ln n} < \frac{1}{n^2 \cdot 1} = \frac{1}{n^2}$$

**Reference series:** $\displaystyle\sum_{n=2}^{\infty}\frac{1}{n^2}$ is a **p-series with $p = 2 > 1$**, which **converges**.

**Apply Comparison Test:**

Since $0 < \frac{1}{n^2 \ln n} \leq \frac{1}{n^2}$ for all $n \geq 3$, and $\sum \frac{1}{n^2}$ converges, by the **Comparison Test**:

$$\sum_{n=2}^{\infty} \frac{1}{n^2 \ln n} \quad \textbf{converges.} \quad \square$$

**Key contrast with M1:** Σ 1/(n ln n) diverges but Σ 1/(n² ln n) converges — the extra factor of n in the denominator makes all the difference. The examiner tested both in 2023 precisely to see if students understood this distinction.

---

## M3. Alternating Series Test

Determine whether each series converges or diverges. For convergent alternating series, state whether convergence is absolute or conditional.

**a)** $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n}$ **[4 marks]**

**b)** $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^n \cdot n}{2n+1}$ **[4 marks]**

**c)** $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^{n+1}}{\sqrt{n}}$ **[4 marks]**

---

### SOLUTION M3

**Part (a): Alternating Harmonic Series**

This is $\sum (-1)^{n-1} b_n$ where $b_n = \frac{1}{n}$.

**Check AST conditions:**
1. $b_{n+1} = \frac{1}{n+1} \leq \frac{1}{n} = b_n$ ✓ (decreasing)
2. $\lim_{n\to\infty} b_n = \lim_{n\to\infty} \frac{1}{n} = 0$ ✓

Both conditions satisfied → series **converges** by the **Alternating Series Test**.

**Absolute convergence?** $\sum |a_n| = \sum \frac{1}{n}$ — the harmonic series, which **diverges** (p=1).

Therefore the alternating harmonic series is **conditionally convergent** (converges, but not absolutely). □

**Part (b):**

$b_n = \frac{n}{2n+1}$.

Check condition 2 first: $\lim_{n\to\infty} \frac{n}{2n+1} = \frac{1}{2} \neq 0$.

Since $\lim b_n \neq 0$, condition 2 of AST fails. Moreover, $\lim a_n = \lim (-1)^n \cdot \frac{n}{2n+1}$ does not exist (oscillates between +1/2 and −1/2).

By the **Divergence Test**: the series **diverges**. □

**Part (c):**

$b_n = \frac{1}{\sqrt{n}}$.

1. $b_{n+1} = \frac{1}{\sqrt{n+1}} \leq \frac{1}{\sqrt{n}} = b_n$ ✓
2. $\lim_{n\to\infty} \frac{1}{\sqrt{n}} = 0$ ✓

→ **Converges** by AST.

**Absolute convergence?** $\sum \frac{1}{\sqrt{n}} = \sum n^{-1/2}$: p-series with $p = \frac{1}{2} \leq 1$ → **diverges**.

Therefore: **conditionally convergent**. □

---

## M4. Ratio Test — Factorials and Exponentials

Determine convergence or divergence using the Ratio Test:

**a)** $\displaystyle\sum_{n=1}^{\infty} \frac{n^3}{3^n}$ **[5 marks]**

**b)** $\displaystyle\sum_{n=0}^{\infty} \frac{(-1)^n \cdot n^3}{n!}$ **[5 marks]**

---

### SOLUTION M4

**Part (a):**

Let $a_n = \frac{n^3}{3^n}$.

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{(n+1)^3}{3^{n+1}} \cdot \frac{3^n}{n^3} = \frac{1}{3} \cdot \left(\frac{n+1}{n}\right)^3 = \frac{1}{3}\left(1+\frac{1}{n}\right)^3$$

$$L = \lim_{n\to\infty} \frac{1}{3}\left(1+\frac{1}{n}\right)^3 = \frac{1}{3}(1)^3 = \frac{1}{3} < 1$$

By the **Ratio Test**: $L = \frac{1}{3} < 1$ → the series **converges absolutely**. □

**Part (b):**

$|a_n| = \frac{n^3}{n!}$.

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{(n+1)^3}{(n+1)!} \cdot \frac{n!}{n^3} = \frac{(n+1)^3}{(n+1) \cdot n!} \cdot \frac{n!}{n^3} = \frac{(n+1)^2}{n^3} = \frac{n^2+2n+1}{n^3}$$

$$L = \lim_{n\to\infty} \frac{n^2+2n+1}{n^3} = \lim_{n\to\infty} \frac{1/n + 2/n^2 + 1/n^3}{1} = 0 < 1$$

By the **Ratio Test**: $L = 0 < 1$ → the series **converges absolutely**. □

*(The $(-1)^n$ sign does not affect the Ratio Test since we take absolute values. Absolute convergence implies convergence.)*

---

## M5. Geometric Series Business Problem — 2025 Style (Paint Layers)

A wall is painted multiple times. The first layer uses **1 litre** of paint, and each subsequent layer uses **half** the paint of the previous one.

**a)** What is the total amount of paint used if the wall is painted infinitely many times? **[5 marks]**

**b)** A second wall is painted with 3 litres on the first coat, and each subsequent coat uses 80% of the previous coat. Find the total paint used and verify the series converges. **[5 marks]**

**c)** A factory releases gas at a rate that decreases by 5% per day. On day 1, it releases 200 kg. What is the total gas released over all days, and should authorities be concerned about infinite total emissions? **[5 marks]**

---

### SOLUTION M5

**Part (a):** [The exact 2025 Q4d question]

Series: $1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \cdots$

$a = 1$, $r = \frac{1}{2}$. Since $|r| = \frac{1}{2} < 1$:

$$S = \frac{1}{1 - \frac{1}{2}} = \frac{1}{\frac{1}{2}} = \boxed{2 \text{ litres}}$$

The total paint used converges to **2 litres**, regardless of how many times the wall is painted.

**Part (b):**

$a = 3$, $r = 0.80$. Since $|r| = 0.80 < 1$, the series converges:

$$S = \frac{3}{1-0.80} = \frac{3}{0.20} = \boxed{15 \text{ litres}}$$

**Verification of convergence:** $|r| = 0.8 < 1$ satisfies the geometric series convergence criterion. Each successive layer uses less paint, and the total remains finite. ✓

**Part (c):**

$a = 200$, $r = 1 - 0.05 = 0.95$. Since $|r| = 0.95 < 1$:

$$S = \frac{200}{1-0.95} = \frac{200}{0.05} = \boxed{4{,}000 \text{ kg total}}$$

**Interpretation:** Although the factory releases gas indefinitely, the total over all time converges to **4,000 kg**. Authorities should evaluate whether this total exceeds safe environmental limits — but mathematically, the emissions are bounded and do not grow without bound. The series converges because the daily rate decays geometrically.

---

### ─────────────────────────────────────
### HARD QUESTIONS (H1 – H4)
### ─────────────────────────────────────

---

## H1. Mixed Test Selection — Five Series, Five Decisions

For each series, state the test used and determine convergence or divergence. Full justification required.

**a)** $\displaystyle\sum_{n=1}^{\infty} \frac{2^n}{n!}$ **[4 marks]**

**b)** $\displaystyle\sum_{n=1}^{\infty} \frac{\ln n}{n}$ **[4 marks]**

**c)** $\displaystyle\sum_{n=1}^{\infty} \left(\frac{3n-1}{4n+2}\right)^n$ **[4 marks]**

**d)** $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^n}{\sqrt[3]{n}}$ **[4 marks]**

**e)** $\displaystyle\sum_{n=1}^{\infty} \frac{1}{n(n+2)}$ **[5 marks]**

---

### SOLUTION H1

**Part (a): $\sum \frac{2^n}{n!}$ — Ratio Test**

$$L = \lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right| = \lim_{n\to\infty}\frac{2^{n+1}}{(n+1)!} \cdot \frac{n!}{2^n} = \lim_{n\to\infty}\frac{2}{n+1} = 0 < 1$$

**Converges absolutely** by the Ratio Test. □

*(Note: this is the series for $e^2 - 1$, which is finite — confirms convergence.)*

**Part (b): $\sum \frac{\ln n}{n}$ — Integral Test**

$f(x) = \frac{\ln x}{x}$ is positive, continuous, and decreasing for $x > e$ (since $f'(x) = \frac{1-\ln x}{x^2} < 0$ for $x > e$).

$$\int_1^\infty \frac{\ln x}{x}\,dx = \left[\frac{(\ln x)^2}{2}\right]_1^\infty = \infty$$

By the **Integral Test**: **diverges**. □

**Part (c): $\sum \left(\frac{3n-1}{4n+2}\right)^n$ — Root Test**

$$L = \lim_{n\to\infty}\sqrt[n]{|a_n|} = \lim_{n\to\infty}\frac{3n-1}{4n+2} = \frac{3}{4} < 1$$

By the **Root Test**: **converges absolutely**. □

**Part (d): $\sum \frac{(-1)^n}{\sqrt[3]{n}}$ — Alternating Series Test**

$b_n = \frac{1}{n^{1/3}}$.

1. $b_{n+1} = \frac{1}{(n+1)^{1/3}} \leq \frac{1}{n^{1/3}} = b_n$ ✓
2. $\lim_{n\to\infty} \frac{1}{n^{1/3}} = 0$ ✓

**Converges** by AST.

*Absolute convergence?* $\sum \frac{1}{n^{1/3}}$: p-series with $p = \frac{1}{3} < 1$ → diverges. Therefore **conditionally convergent**. □

**Part (e): $\sum \frac{1}{n(n+2)}$ — Telescoping Series**

Use partial fractions:

$$\frac{1}{n(n+2)} = \frac{1}{2}\left(\frac{1}{n} - \frac{1}{n+2}\right)$$

Partial sums telescope:

$$s_N = \frac{1}{2}\sum_{n=1}^N\left(\frac{1}{n}-\frac{1}{n+2}\right) = \frac{1}{2}\left[\left(\frac{1}{1}-\frac{1}{3}\right)+\left(\frac{1}{2}-\frac{1}{4}\right)+\left(\frac{1}{3}-\frac{1}{5}\right)+\cdots\right]$$

After cancellation, only the first two positive terms and the last two negative terms survive:

$$s_N = \frac{1}{2}\left(1 + \frac{1}{2} - \frac{1}{N+1} - \frac{1}{N+2}\right)$$

$$S = \lim_{N\to\infty}s_N = \frac{1}{2}\left(1+\frac{1}{2}\right) = \frac{1}{2}\cdot\frac{3}{2} = \boxed{\frac{3}{4}}$$

The series **converges** to $\dfrac{3}{4}$. □

---

## H2. The Predicted 2026 Pair — Ratio Test + Integral Test Together

This question mirrors the two-part convergence structure in 2023 Q4c and 2025 Q4e:

**i.** Determine whether $\displaystyle\sum_{n=1}^{\infty} \frac{n \cdot 4^n}{(n+1)!}$ converges or diverges. **[5 marks]**

**ii.** Determine whether $\displaystyle\sum_{n=2}^{\infty} \frac{1}{n(\ln n)^2}$ converges or diverges. **[5 marks]**

---

### SOLUTION H2

**Part (i): Ratio Test**

$a_n = \frac{n \cdot 4^n}{(n+1)!}$

$$\left|\frac{a_{n+1}}{a_n}\right| = \frac{(n+1)\cdot 4^{n+1}}{(n+2)!}\cdot\frac{(n+1)!}{n \cdot 4^n} = \frac{4(n+1)^2}{n(n+2)}$$

Wait — let me be careful:

$$= \frac{(n+1) \cdot 4 \cdot 4^n}{(n+2)(n+1)!} \cdot \frac{(n+1)!}{n \cdot 4^n} = \frac{4(n+1)}{n(n+2)}$$

$$L = \lim_{n\to\infty}\frac{4(n+1)}{n(n+2)} = \lim_{n\to\infty}\frac{4n+4}{n^2+2n} = \lim_{n\to\infty}\frac{4/n + 4/n^2}{1+2/n} = \frac{0}{1} = 0 < 1$$

By the **Ratio Test**: **converges absolutely**. □

*(The factorial in the denominator grows much faster than $4^n$, so the series converges.)*

**Part (ii): Integral Test**

$f(x) = \frac{1}{x(\ln x)^2}$. This is positive and continuous on $[2, \infty)$.

Check decreasing: $f'(x) < 0$ for $x > 1$ (both $x$ and $(\ln x)^2$ are increasing). ✓

$$\int_2^\infty \frac{1}{x(\ln x)^2}\,dx$$

Let $u = \ln x$, $du = \frac{dx}{x}$:

$$= \int_{\ln 2}^\infty \frac{1}{u^2}\,du = \left[-\frac{1}{u}\right]_{\ln 2}^\infty = 0 - \left(-\frac{1}{\ln 2}\right) = \frac{1}{\ln 2} < \infty$$

The integral **converges**.

By the **Integral Test**: $\displaystyle\sum_{n=2}^\infty \frac{1}{n(\ln n)^2}$ **converges**. □

**Key contrast with M1:** $\sum \frac{1}{n \ln n}$ diverges (integral = ∞) but $\sum \frac{1}{n(\ln n)^2}$ converges (integral is finite). The square on ln n is the difference — the examiner may test both in 2026 as a deliberate trap.

---

## H3. Absolute vs Conditional Convergence — Deep Analysis

For each series, determine: (a) does it converge? (b) is convergence absolute or conditional?

**i.** $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^n \cdot n}{n^2+1}$ **[6 marks]**

**ii.** $\displaystyle\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2}$ **[4 marks]**

---

### SOLUTION H3

**Part (i):**

$b_n = \frac{n}{n^2+1}$.

**Step 1 — Check AST conditions:**

$b_{n+1} \leq b_n$? Check: $\frac{n+1}{(n+1)^2+1} \leq \frac{n}{n^2+1}$

Cross multiply (all positive): $(n+1)(n^2+1) \leq n((n+1)^2+1)$

LHS: $n^3+n+n^2+1$

RHS: $n(n^2+2n+2) = n^3+2n^2+2n$

LHS − RHS $= n^3+n^2+n+1 - n^3-2n^2-2n = -n^2-n+1$

For $n \geq 1$: $-n^2-n+1 \leq -1 < 0$. So LHS < RHS, confirming $b_{n+1} < b_n$. ✓

$\lim_{n\to\infty}\frac{n}{n^2+1} = \lim \frac{1/n}{1+1/n^2} = 0$ ✓

By **AST**: the series **converges**.

**Step 2 — Absolute convergence?**

$\sum\left|\frac{(-1)^n n}{n^2+1}\right| = \sum\frac{n}{n^2+1}$

For large $n$: $\frac{n}{n^2+1} \approx \frac{n}{n^2} = \frac{1}{n}$.

**Limit Comparison Test** with $b_n = 1/n$:

$$\lim_{n\to\infty}\frac{n/(n^2+1)}{1/n} = \lim_{n\to\infty}\frac{n^2}{n^2+1} = 1 > 0$$

Since $\sum 1/n$ **diverges** and the limit is a positive finite number, $\sum \frac{n}{n^2+1}$ **diverges** by the Limit Comparison Test.

**Conclusion:** The series is **conditionally convergent** (converges, but not absolutely). □

**Part (ii):**

$\sum \frac{(-1)^n}{n^2}$.

**Absolute convergence first:** $\sum \frac{1}{n^2}$ is a p-series with $p = 2 > 1$ → **converges**.

Since the series converges absolutely, it also converges (absolutely convergent ⟹ convergent).

**Conclusion:** **Absolutely convergent**. □

---

## H4. Sri Lankan Business Context — Multi-Part Series Application [Predicted 2026 Style]

A Sri Lankan exporter's revenue from a new product is modelled as follows:
- In month 1, the product earns **LKR 480,000**.
- Each subsequent month, revenue is **75% of the previous month's** (due to market saturation).

**a)** Find the total revenue over the product's lifetime. **[5 marks]**

**b)** The exporter wants the total revenue to exceed LKR 1.5 million. Is this achievable? If the initial revenue were instead LKR $a$, find the minimum value of $a$ that achieves this. **[4 marks]**

**c)** A competitor enters the market in month 3. From month 3 onward, the exporter's monthly revenue drops by an additional 10% compounding on top of the existing 25% decline (so from month 3 onward, each month is 67.5% of the previous). Recalculate the total lifetime revenue. **[6 marks]**

---

### SOLUTION H4

**Part (a):**

$a = 480{,}000$, $r = 0.75$. Since $|r| < 1$:

$$S = \frac{480{,}000}{1-0.75} = \frac{480{,}000}{0.25} = \boxed{\text{LKR }1{,}920{,}000}$$

**Part (b):**

$S = 1{,}920{,}000 > 1{,}500{,}000$. Yes — the total revenue **exceeds LKR 1.5 million**. ✓

For general initial revenue $a$: $S = \frac{a}{0.25} = 4a$.

Require $4a \geq 1{,}500{,}000 \implies a \geq 375{,}000$.

Minimum initial revenue: **LKR 375,000**. □

**Part (c):**

Revenue by month:
- Month 1: 480,000
- Month 2: 480,000 × 0.75 = 360,000
- Month 3 onward: geometric with first term = 360,000 × 0.675 = 243,000, ratio = 0.675

Total = (Months 1 and 2) + (geometric series from month 3)

Sum of months 1 and 2: $480{,}000 + 360{,}000 = 840{,}000$

Geometric series from month 3: $a' = 243{,}000$, $r' = 0.675$. Since $|r'| < 1$:

$$S' = \frac{243{,}000}{1-0.675} = \frac{243{,}000}{0.325} = 747{,}692.31$$

**Total lifetime revenue:**

$$S_{\text{total}} = 840{,}000 + 747{,}692 \approx \boxed{\text{LKR }1{,}587{,}692}$$

The competitor's entry reduces total lifetime revenue from LKR 1,920,000 to approximately LKR 1,587,692 — a reduction of about LKR 332,308.

---

### ─────────────────────────────────────
### NIGHTMARE QUESTIONS (N1 – N2)
### ─────────────────────────────────────

---

## N1. The Complete Convergence Test Proof — Geometric Series

**a)** Prove that the geometric series $\displaystyle\sum_{n=1}^{\infty}ar^{n-1}$ converges to $\dfrac{a}{1-r}$ when $|r| < 1$, and diverges when $|r| \geq 1$. **[8 marks]**

**b)** Use your proof to explain why the result $S = \frac{a}{1-r}$ gives the TOTAL (infinite) sum, not just a partial sum. **[4 marks]**

---

### SOLUTION N1

**Part (a): Proof**

The $N$th partial sum of the geometric series is:

$$s_N = a + ar + ar^2 + \cdots + ar^{N-1} = \sum_{n=1}^N ar^{n-1}$$

**Closed form for $s_N$:**

Multiply both sides by $r$:

$$rs_N = ar + ar^2 + \cdots + ar^N$$

Subtract: $s_N - rs_N = a - ar^N$

$$s_N(1-r) = a(1-r^N)$$

For $r \neq 1$:

$$s_N = \frac{a(1-r^N)}{1-r} \quad \cdots (*)$$

**Case 1: $|r| < 1$**

$\lim_{N\to\infty}r^N = 0$ (since $|r| < 1$).

$$S = \lim_{N\to\infty}s_N = \frac{a(1-0)}{1-r} = \frac{a}{1-r}$$

The series **converges** to $\dfrac{a}{1-r}$. □

**Case 2: $|r| > 1$**

$|r^N| \to \infty$ as $N \to \infty$, so $s_N$ has no finite limit. The series **diverges**. □

**Case 3: $r = 1$**

$s_N = a + a + \cdots + a = Na \to \infty$. **Diverges**. □

**Case 4: $r = -1$**

$s_N$ alternates between $a$ and $0$ — no limit exists. **Diverges**. □

Therefore: converges iff $|r| < 1$, diverges otherwise. □

**Part (b):**

The formula $S = \frac{a}{1-r}$ is the **limit** of the sequence of partial sums $\{s_N\}$ as $N \to \infty$. From (*):

$$S = \lim_{N\to\infty}\frac{a(1-r^N)}{1-r} = \frac{a}{1-r}$$

because $r^N \to 0$. This limit represents the value that the running total approaches as we add infinitely many terms — it is the exact sum of all infinitely many terms, not an approximation. In the business context (e.g., total lifetime profit), it represents the cumulative result of infinitely many (though geometrically shrinking) payments.

---

## N2. The Hardest Possible Q4 — Combined Reasoning

**a)** A company's monthly revenue follows a geometric series with first term $a$ and ratio $r$ where $0 < r < 1$. The company claims their total lifetime revenue will be exactly **LKR 2.4 million**, and that revenue in month 2 will be **LKR 360,000**. Find $a$ and $r$. **[5 marks]**

**b)** Determine whether the following series converges or diverges. Identify the most efficient test and justify your choice before applying it.

$$\sum_{n=1}^{\infty} \frac{n! \cdot 3^n}{(2n)!}$$

**[6 marks]**

**c)** Two students disagree about $\displaystyle\sum_{n=1}^{\infty}\frac{\cos(n\pi)}{n}$.

- Student A says: "The terms go to zero, so it converges."
- Student B says: "Apply the Divergence Test: $\cos(n\pi) = (-1)^n$ and $(-1)^n/n \to 0$, so the test is inconclusive. We need the AST."

Who is correct? Apply the correct test and determine convergence. **[6 marks]**

**d)** True or False (with proof or counterexample): "If $\sum a_n$ and $\sum b_n$ both diverge, then $\sum (a_n + b_n)$ diverges." **[4 marks]**

---

### SOLUTION N2

**Part (a):**

Month 2 revenue = $ar = 360{,}000$ … (i)

Total: $\frac{a}{1-r} = 2{,}400{,}000$ … (ii)

From (ii): $a = 2{,}400{,}000(1-r)$.

Substitute into (i): $2{,}400{,}000(1-r)r = 360{,}000$

$2400(1-r)r = 360$ (divide by 1000)

$r - r^2 = \frac{360}{2400} = 0.15$

$r^2 - r + 0.15 = 0$

$$r = \frac{1 \pm \sqrt{1-0.6}}{2} = \frac{1 \pm \sqrt{0.4}}{2} = \frac{1 \pm 0.6325}{2}$$

$r_1 = \frac{1.6325}{2} = 0.816$ or $r_2 = \frac{0.3675}{2} = 0.184$

Both are in $(0,1)$. From $a = 2{,}400{,}000(1-r)$:

- If $r = 0.816$: $a = 2{,}400{,}000(0.184) = 441{,}600$. Check: $ar = 441{,}600(0.816) \approx 360{,}346 \neq 360{,}000$ exactly (rounding).

Let me solve exactly: $r = \frac{1 \pm \sqrt{2/5}}{2}$.

With $r_2 = \frac{1-\sqrt{2/5}}{2}$: $a = 360{,}000/r_2$.

For exam purposes, the clean solution is: $r = 0.75$, $a = 480{,}000$, check: $ar = 360{,}000$ ✓, total $= 480{,}000/0.25 = 1{,}920{,}000 \neq 2{,}400{,}000$.

Try $r = 0.8$: total $= a/0.2 = 5a$; $ar = 0.8a = 360{,}000 \implies a = 450{,}000$; total $= 5(450{,}000) = 2{,}250{,}000 \neq 2{,}400{,}000$.

Try $r = 0.85$: $a = 360{,}000/0.85 = 423{,}529$; total $= 423{,}529/0.15 = 2{,}823{,}529 \neq 2{,}400{,}000$.

The exact values come from the quadratic. The quadratic gives:

$r^2-r+0.15=0 \implies r = \frac{1 \pm\sqrt{0.4}}{2}$.

$\sqrt{0.4} = \sqrt{2/5} = \frac{\sqrt{10}}{5} \approx 0.6325$.

$r_1 \approx 0.816$, $r_2 \approx 0.184$.

For $r_1 = 0.816$: $a = 360{,}000/0.816 \approx 441{,}176$; total $\approx 441{,}176/0.184 \approx 2{,}400{,}000$ ✓

$\boxed{r \approx 0.816, \quad a \approx \text{LKR }441{,}176}$

(or the second solution $r \approx 0.184$, $a \approx 1{,}956{,}522$ — both valid mathematically; the first is more realistic for a declining revenue scenario.)

**Part (b):**

$a_n = \frac{n!\cdot 3^n}{(2n)!}$. Contains $n!$ and $3^n$ → **Ratio Test** is most efficient.

$$\frac{a_{n+1}}{a_n} = \frac{(n+1)!\cdot 3^{n+1}}{(2n+2)!}\cdot\frac{(2n)!}{n!\cdot 3^n}$$

$$= \frac{(n+1)\cdot 3}{(2n+2)(2n+1)} = \frac{3(n+1)}{2(n+1)(2n+1)} = \frac{3}{2(2n+1)}$$

$$L = \lim_{n\to\infty}\frac{3}{2(2n+1)} = 0 < 1$$

By the **Ratio Test**: **converges absolutely**. □

*($(2n)!$ grows much faster than $n!\cdot 3^n$.)*

**Part (c):**

**Student B is correct.**

Note: $\cos(n\pi) = (-1)^n$, so the series is $\displaystyle\sum_{n=1}^\infty \frac{(-1)^n}{n}$.

Student A is wrong: "$a_n \to 0$" does not imply convergence (harmonic series counterexample). The Divergence Test only gives divergence when $\lim a_n \neq 0$ — it cannot conclude convergence.

Student B correctly identifies this as an alternating series requiring the **Alternating Series Test**.

Apply AST with $b_n = \frac{1}{n}$:
1. $b_{n+1} = \frac{1}{n+1} < \frac{1}{n} = b_n$ ✓
2. $\lim_{n\to\infty}\frac{1}{n} = 0$ ✓

**Conclusion:** $\displaystyle\sum_{n=1}^\infty\frac{(-1)^n}{n}$ **converges** (conditionally — since $\sum 1/n$ diverges). □

**Part (d): FALSE**

**Counterexample:** Let $a_n = \frac{1}{n}$ and $b_n = -\frac{1}{n}$.

Both $\sum a_n = \sum \frac{1}{n}$ (harmonic series) and $\sum b_n = \sum (-\frac{1}{n})$ **diverge**.

But $\sum(a_n+b_n) = \sum\left(\frac{1}{n}-\frac{1}{n}\right) = \sum 0 = 0$, which **converges** (to 0). □

The statement is **FALSE**. The sum of two divergent series can converge.

---

## SECTION E: RAPID-FIRE REVISION

| Situation | Action |
|-----------|--------|
| $\lim a_n \neq 0$ | Divergence Test — done immediately, no other test needed |
| $|r| < 1$ geometric | Converges to $a/(1-r)$; write $a$ and $r$ explicitly |
| $\sum 1/n^p$ | $p > 1$ converges; $p \leq 1$ diverges |
| $(-1)^n b_n$ | Alternating Series Test — check BOTH conditions |
| Contains $n!$ or $k^n$ | Ratio Test — show full limit calculation |
| $(b_n)^n$ form | Root Test — take nth root and find limit |
| $\sum 1/(n \ln n)$ | Integral Test — substitution $u = \ln x$ — **diverges** |
| $\sum 1/(n^2 \ln n)$ | Comparison with $1/n^2$ — **converges** |
| $\sum 1/(n(\ln n)^2)$ | Integral Test — substitution $u = \ln x$ — **converges** |
| Business profit/geometric | Write $a$ = first value, $r$ = ratio (decrease → $r = 1-k$) |
| Verify geometric convergence | State $\|r\| < 1$ explicitly before computing sum |

---

*End of Topic 12: Infinite Series & Convergence Tests*
*Total: 4 Easy + 5 Medium + 4 Hard + 2 Nightmare = 15 questions with full solutions*
*Next: Topic 14 — Taylor & Maclaurin Series*
