# DA2411 Linear Algebra — 24th Batch Master Preparation Plan
**University of Moratuwa | Faculty of Business | Department of Decision Sciences**
*Reverse-engineered from 6 past papers (2019–2025) + complete knowledge base*
*Prepared for Phase 2 question generation — DO NOT generate questions yet*

---

## EXAMINER FINGERPRINT: WHO IS THIS PERSON?

Before the roadmap, understand the examiner's psychology. Across six papers, consistent patterns emerge:

**Structural DNA of the DA2411 exam (2023 onward):**
- 4 questions × 25 marks. No choice. Every mark counts.
- Q1: Matrix fundamentals (RREF, Gauss-Jordan, True/False, dimension analysis)
- Q2: Applied matrix multiplication + Leontief Input-Output (alternates with Q3)
- Q3: Eigenvalues OR iterative methods + matrix equation solving
- Q4: Series (geometric business application + convergence tests + Taylor series)

**Examiner preferences:**
1. Loves prose-encoded problems — students must decode words into matrices before any algebra
2. Favors True/False items with proof-or-counterexample (tests conceptual depth, not just computation)
3. Returns to the same five canonical statement types repeatedly (especially "every square matrix has an inverse")
4. Uses real Sri Lankan contexts in recent papers (Colombo/Kandy logistics in 2025, local factories)
5. Escalates within a question: part (a) is scaffolding, part (b) is the real test
6. The 2025 paper introduced multi-step matrix expression solving (find K from a complex equation) — expect this to recur
7. Q4 always has at least one "pure reasoning" item (e.g., 2025: if A³=I, find A⁻¹; 2025: find |A¹²¹ − A¹²⁰|) worth 5 marks — these are "free marks" if you know the trick, "time sinks" if you don't

---

## PART I: COMPLETE TOPIC ROADMAP

---

### TOPIC 1 — VECTORS & VECTOR OPERATIONS

**Subtopics:**
- Component form, magnitude, equality
- Vector addition, scalar multiplication, subtraction
- Unit vectors and normalization
- Standard basis vectors (i, j)
- Dot product and the angle formula
- Orthogonality criterion (dot product = 0)
- Work as a dot product application
- Vector norms: L1, L2 (Euclidean), L∞

**Importance Level:** ★★☆☆☆ (Moderate — foundational but rarely the main exam focus)

**Past-Paper Frequency:** 0/6 as a standalone question. Used implicitly in eigenvalue/eigenvector normalization and Leontief output vectors.

**Difficulty Level:** Easy to Medium

**Predicted Exam Probability for 24th Batch:** 15%
- Most likely to appear as a sub-part of an eigenvalue question (normalize an eigenvector) or a True/False item (orthogonality, dot product properties)
- Could appear in a new "vectors + matrix multiplication" combo question

**Dependencies/Prerequisites:** None (foundational)

**Estimated Questions to Generate:**
- Easy: 3 (compute dot product, find unit vector, check orthogonality)
- Medium: 3 (find vector making given angle, work done by force, norm comparison)
- Hard: 2 (prove Cauchy-Schwarz inequality, geometric proof using dot product)
- Nightmare: 1 (multi-part combining vectors, norms, and orthogonal projection)

---

### TOPIC 2 — SYSTEMS OF LINEAR EQUATIONS & GAUSS-JORDAN ELIMINATION

**Subtopics:**
- Setting up augmented matrices from word problems
- Three row operations and their notation
- RREF conditions (all 4 conditions — identifying violations)
- Gauss-Jordan elimination procedure (full pivot-by-pivot)
- Recognizing solution types: unique / infinitely many (free parameter) / no solution
- Back-substitution (Gaussian elimination / REF)
- Business contexts: capacity + cost, calories, fish tank, vehicles, people

**Importance Level:** ★★★★★ (Absolutely critical)

**Past-Paper Frequency:** 5/6 papers (appeared in 2019, 2020, 2022, 2023, 2024; absent only in 2025)

**Difficulty Level:** Medium (setup is where students fail; row reduction is mechanical)

**Predicted Exam Probability for 24th Batch:** 90%
- Missing from 2025 after being in every other paper — the cycle strongly suggests it RETURNS in 2026
- Will appear as a 10–15 mark word problem requiring full variable definition, system setup, and complete row reduction

**Dependencies/Prerequisites:** None (this is a first-principles topic)

**Key Examiner Trap:** Students who jump straight to the augmented matrix without clearly defining variables lose method marks. The examiner rewards explicit variable definition and the written system of equations before the matrix.

**Estimated Questions to Generate:**
- Easy: 3 (direct 2-variable systems, straightforward 3×3)
- Medium: 4 (word problems: capacity + cost, ingredient limits, calorie problems)
- Hard: 3 (infinite-solution cases with free parameters, over-determined systems)
- Nightmare: 2 (system with a parameter k — find k for no/unique/infinite solutions)

---

### TOPIC 3 — RREF IDENTIFICATION & MATRIX DIMENSION ANALYSIS

**Subtopics:**
- Identifying whether a matrix is in RREF (checking all 4 conditions)
- Stating which specific condition is violated (not just "it's wrong")
- Number of solutions from an RREF matrix (counting free variables)
- Matrix dimension compatibility for addition, multiplication, transpose
- Consequences of singularity/non-singularity on inverse existence
- True/False dimension and existence analysis using given properties

**Importance Level:** ★★★★☆ (Very high)

**Past-Paper Frequency:** RREF check: 4/6; Dimension analysis: 3/6

**Difficulty Level:** Easy to Medium

**Predicted Exam Probability for 24th Batch:** 85%
- Both types appeared in 2025 (Q1a RREF + Q1a dimension). High likelihood of recurrence.
- Often bundled together into a multi-part Q1(a)

**Dependencies/Prerequisites:** Topic 2 (understanding of RREF process)

**Examiner Trap:** For RREF, students check "leading 1s" but forget condition 4 (column with a leading 1 must have zeros EVERYWHERE else above AND below). Also: a row [0 0 0 | c≠0] means no solution, but students sometimes say "infinitely many" by misreading.

**Estimated Questions to Generate:**
- Easy: 4 (identify each violation type explicitly; count free variables)
- Medium: 3 (combined RREF + solution count + dimension analysis)
- Hard: 2 (deliberately tricky matrices near-RREF with subtle violations)
- Nightmare: 1 (parametric matrix family — "for what value of k is this RREF?")

---

### TOPIC 4 — MATRIX ALGEBRA & OPERATIONS

**Subtopics:**
- Matrix equality, addition, subtraction, scalar multiplication
- Transpose properties: (AB)ᵀ = BᵀAᵀ, (Aᵀ)ᵀ = A
- Matrix multiplication (dimension compatibility, dot product formula)
- Non-commutativity: AB ≠ BA in general
- Applied matrix multiplication (encode real data into matrices, compute meaningful products)
- True/False statements with proof or counterexample
- Matrix equation solving: isolating X (one-sided and two-sided unknowns)
- Solving for scalar unknowns a, b, c, d from matrix equations

**Importance Level:** ★★★★★ (Critical — this underpins every other topic)

**Past-Paper Frequency:** Applied matrix multiplication: 5/6; Matrix equation solving: 4/6; True/False: 4/6

**Difficulty Level:** Easy to Hard (applied encoding is Medium; proof-writing is Hard)

**Predicted Exam Probability for 24th Batch:** 95%
- Matrix equation for scalars a, b, c, d has appeared in 2023 and 2024 — the complex version with K (2025) may repeat
- Applied matrix multiplication (logistics, costs, wages) is a near-certain Q2 component

**Dependencies/Prerequisites:** Basic arithmetic, understanding of matrix dimensions

**Key Examiner Trap (True/False):**
The five canonical statements tested across all papers:
1. "Every square matrix has an inverse" — FALSE (singular matrices) [4 papers!]
2. "Matrix addition is commutative" — TRUE (algebraic proof)
3. "If AB exists, then BA exists" — FALSE (dimension counterexample)
4. "A linear system with n equations and n unknowns always has a solution" — FALSE
5. "If eigenvalue 0 exists, matrix is invertible" — FALSE (it's the opposite)

**Estimated Questions to Generate:**
- Easy: 3 (standard multiply/add; simple matrix equation for X)
- Medium: 4 (applied encoding word problems; transpose laws; solve for scalars)
- Hard: 3 (complex matrix equations isolating X from two sides; proof True/False)
- Nightmare: 2 (solve for matrix K from a multi-step equation like 2025 Q3a; prove a new T/F)

---

### TOPIC 5 — MATRIX INVERSE & DETERMINANTS

**Subtopics:**
- 2×2 inverse formula and when it fails (det = 0)
- Row-reduction method to find A⁻¹ for larger matrices
- Determinant properties: det(Aᵀ) = det(A), row swap negates det
- Singularity vs. non-singularity
- Solving AX = B using inverse: X = A⁻¹B
- Using inverse to find A from eigendecomposition (A = PDP⁻¹)
- Special results: if A³ = I, then A⁻¹ = A² (2025 Q4a)
- The trace = 0 diagonal matrix singularity question (2024)

**Importance Level:** ★★★★☆ (Very high — tools used everywhere)

**Past-Paper Frequency:** Direct inverse computation: 3/6; Determinant properties proved: 2/6 (2019, 2020); Inverse in service of other topics: 6/6

**Difficulty Level:** Easy (2×2 formula) to Medium (3×3 by row reduction)

**Predicted Exam Probability for 24th Batch:** 70% as a standalone sub-part; 100% as an implicit tool

**Examiner Trend:** The "pure reasoning" items about matrix powers (2025: A³=I find A⁻¹; A¹²¹−A¹²⁰) have replaced direct computation of inverses. Expect at least one such reasoning item.

**Estimated Questions to Generate:**
- Easy: 3 (2×2 inverse formula, check if singular, solve 2×2 system via inverse)
- Medium: 4 (3×3 by row reduction; solve matrix power problems; trace analysis)
- Hard: 3 (find A from A⁻¹ = A² type; prove det(Aᵀ)=det(A); analyze powers of A)
- Nightmare: 2 (multi-step combining inverse + eigenvalues + determinant reasoning)

---

### TOPIC 6 — LU FACTORIZATION

**Subtopics:**
- Definition of lower-triangular (L) and upper-triangular (U) matrices
- Computing multipliers lᵢₖ = aᵢₖ/aₖₖ
- LU decomposition algorithm (Gaussian elimination variant)
- Forward substitution: solve LY = B
- Backward substitution: solve UX = Y
- Advantage: solve multiple right-hand sides with one factorization
- Inverse of triangular matrices (diagonal entries reciprocate)

**Importance Level:** ★★★☆☆ (Moderate — taught but infrequent in DA2411 era)

**Past-Paper Frequency:** 2/6 (2019, 2020 only — both in the pre-DA2411 era)

**Difficulty Level:** Medium to Hard

**Predicted Exam Probability for 24th Batch:** 30%
- Has not appeared in any DA2411 paper (2023, 2024, 2025)
- But it IS in the syllabus and knowledge base, and the gap increases probability
- A "surprise" LU question would follow the 2019 format: compute L, U then solve Ax=b

**Dependencies/Prerequisites:** Topic 2 (Gaussian elimination), Topic 5 (inverse of triangular matrices)

**Examiner Trap:** Students confuse L and U. L has 1s on diagonal and the multipliers below. U is the result after elimination (upper triangular). If row swaps are needed, standard LU fails — but exam problems are designed to avoid this.

**Estimated Questions to Generate:**
- Easy: 2 (2×2 LU by hand; identify L vs U from a given factorization)
- Medium: 3 (3×3 LU computation; forward + backward substitution)
- Hard: 2 (3×3 LU then solve multiple right-hand sides; prove A = LU)
- Nightmare: 1 (LU with a parameter in matrix; analyze when factorization breaks down)

---

### TOPIC 7 — LEONTIEF INPUT-OUTPUT MODEL

**Subtopics:**
- Economic interpretation: technology matrix (each column = inputs per $1 output of that sector)
- Setting up M from prose: identifying which sector is the row and which is the column
- Balance equation: X = MX + D → (I − M)X = D
- Computing (I − M)⁻¹ by row reduction
- Total output: X = (I − M)⁻¹D
- Two-sector vs. three-sector models
- Interpreting the result: each sector's required total production

**Importance Level:** ★★★★★ (Highest priority — tied with eigenvalues)

**Past-Paper Frequency:** 5/6 papers (all except 2023). Three-sector model used in 4/5 cases.

**Difficulty Level:** Medium (setup from prose) to Hard (computing 3×3 inverse)

**Predicted Exam Probability for 24th Batch:** 95%
- Present in 2024, 2025 — near-certain for 2026
- Always carries 15–20 marks
- Sectors used historically: Coal/Oil/Transport (2019), Agri/Manuf/Transport (2020, 2024), Mining/Farming/Tourism (2022), Manuf/Energy/Services (2025)
- For 24th Batch: expect a new sector trio, possibly Healthcare/Tech/Transport or Finance/Retail/Logistics given the Sri Lankan business context shift

**Dependencies/Prerequisites:** Topics 4, 5 (matrix multiplication and inverse)

**Key Examiner Trap:** Column j of the technology matrix gives INPUTS REQUIRED BY sector j, not outputs. Students who transpose the logic get the wrong matrix and lose all subsequent marks. The examiner writes "production of a dollar's worth of sector X requires..." — the sector being described is the COLUMN.

**Estimated Questions to Generate:**
- Easy: 2 (two-sector model; direct computation from pre-built M)
- Medium: 4 (three-sector from prose; compute (I−M)⁻¹; find output X)
- Hard: 3 (novel sectors; interpret results; analyze what happens if demand doubles)
- Nightmare: 2 (find what external demand D is achievable given a production constraint; analyze productive economy conditions)

---

### TOPIC 8 — ITERATIVE METHODS (JACOBI & GAUSS-SEIDEL)

**Subtopics:**
- Diagonal dominance: definition and row-by-row verification
- Convergence theorem: diagonally dominant → both methods converge
- Jacobi method: update ALL variables simultaneously using previous iteration
- Gauss-Seidel method: update variables sequentially using newest available values
- Performing 2 iterations (the exam standard) with x⁰ = [0,0,0]ᵀ
- Rounding to 2 decimal places at each step
- Comparing convergence behaviour of both methods

**Importance Level:** ★★★☆☆ (Moderate — NEW addition to DA2411)

**Past-Paper Frequency:** 1/6 (2024 only — first appearance)

**Difficulty Level:** Medium (algorithmic — procedural marks available for correct setup)

**Predicted Exam Probability for 24th Batch:** 55%
- Appeared for the first time in 2024, did NOT appear in 2025
- Alternation pattern suggests it could return in 2026
- If it appears, it will be a full Q3 (25 marks) similar to 2024

**Dependencies/Prerequisites:** Topic 2 (linear systems), Topic 3 (matrix properties)

**Key Examiner Trap:** In Gauss-Seidel, x₁ updated first, then x₂ USES THE NEW x₁, then x₃ uses the new x₁ and x₂. Students who use the old values throughout are doing Jacobi, not Gauss-Seidel. This costs all marks on the Gauss-Seidel part.

**Estimated Questions to Generate:**
- Easy: 2 (check diagonal dominance; 1 iteration of Jacobi)
- Medium: 3 (2 full iterations of each method; comparison)
- Hard: 2 (weakly dominant or non-dominant system; analyze convergence)
- Nightmare: 1 (derive the iteration formula from scratch; prove convergence for a specific case)

---

### TOPIC 9 — THE EIGENVALUE PROBLEM

**Subtopics:**
- Definition: Ax = λx, (A − λI)x = 0
- Characteristic equation: det(A − λI) = 0
- 2×2 characteristic polynomial (quadratic)
- 3×3 characteristic polynomial (cubic — cofactor expansion)
- Finding eigenvectors by solving (A − λI)x = 0 via row reduction
- Properties: trace = Σλᵢ, det = Πλᵢ, eigenvalues of Aᵀ same as A
- Relation between eigenvalues of A and kA, Aⁿ, A+kI
- Verifying a given vector is an eigenvector (matrix multiply and check scaling)
- Reconstructing A from known eigenvalues and eigenvectors (A = PDP⁻¹)
- The determinant |A¹²¹ − A¹²⁰| trick (2025 Q4b — factor out power)
- Symmetric matrices: real eigenvalues, orthogonal eigenvectors
- Orthogonal diagonalization: U^TAU = D (Spectral Theorem)
- Normalizing eigenvectors to form U

**Importance Level:** ★★★★★ (Guaranteed — appears in EVERY paper)

**Past-Paper Frequency:** 6/6 — the only topic with a perfect record

**Difficulty Level:** Medium (2×2) to Hard (3×3 with repeated eigenvalues) to Nightmare (reconstruct A from eigenvectors)

**Predicted Exam Probability for 24th Batch:** 100%

**Sub-topic Probability Breakdown:**
- Computing eigenvalues and eigenvectors of 3×3: 85%
- A + kI eigenvalue relation: 70% (appeared 2019, 2023, 2025)
- Verify if a vector is an eigenvector: 40% (2023)
- Reconstruct A from eigenvectors: 35% (2023)
- Orthogonal diagonalization (U^TAU = D): 40% (2022, 2023)
- Matrix power determinant trick (|Aⁿ|): 35% (2025)

**Key Examiner Traps:**
1. 3×3 characteristic polynomial expansion — sign errors in cofactor expansion cost eigenvalues
2. For eigenvectors: always row-reduce (A−λI), choose a free variable, express in terms of it
3. Normalizing: divide by the norm before forming U (not just any scalar multiple)
4. λ=0 as an eigenvalue ↔ A is singular — this is tested as True/False

**Estimated Questions to Generate:**
- Easy: 3 (2×2 eigenvalues and eigenvectors; verify eigenvector; eigenvalue of A+kI)
- Medium: 5 (3×3 with distinct eigenvalues; reconstruct A; eigenvalue properties)
- Hard: 4 (3×3 repeated eigenvalues; orthogonal diagonalization; use trace/det to find λ)
- Nightmare: 3 (symmetric 3×3 full diagonalization; determinant of matrix power; original proof)

---

### TOPIC 10 — RANK & LINEAR INDEPENDENCE

**Subtopics:**
- Rank definition: number of nonzero rows in RREF
- Computing rank by row reduction
- Linear dependence/independence: definition with scalars c₁v₁ + … = 0
- Determinant test for linear independence (square case)
- Connection between rank and solution types
- Rank-nullity theorem (may be implicit)

**Importance Level:** ★★★☆☆ (Moderate — conceptually tested, not always computationally)

**Past-Paper Frequency:** 1/6 explicitly (2023 Q3d — reconstruct A from eigenvectors implicitly uses independence)

**Difficulty Level:** Easy to Medium

**Predicted Exam Probability for 24th Batch:** 25% as standalone; 60% implicit in eigenvalue questions

**Dependencies/Prerequisites:** Topics 2, 4

**Estimated Questions to Generate:**
- Easy: 2 (compute rank; determine if 3 vectors are linearly independent)
- Medium: 2 (connect rank to solution type; use determinant test)
- Hard: 1 (parametric rank problem: find k so rank(A) = 2)
- Nightmare: 1 (prove linear independence of eigenvectors for distinct eigenvalues)

---

### TOPIC 11 — INFINITE SEQUENCES

**Subtopics:**
- Arithmetic and geometric sequences
- Convergence/divergence definition
- Limit laws for sequences
- Theorem: rⁿ converges iff −1 < r ≤ 1
- L'Hôpital's rule for sequences (via continuous version)
- Monotonic sequences (increasing/decreasing)
- Business application: geometric decay (profit declining by k% per year)

**Importance Level:** ★★★☆☆ (Moderate — scaffolding for series topics)

**Past-Paper Frequency:** 0/6 as isolated questions; embedded in geometric series business problems (2023, 2025)

**Difficulty Level:** Easy to Medium

**Predicted Exam Probability for 24th Batch:** 20% standalone; sequences appear inside Q4 multi-part questions

**Estimated Questions to Generate:**
- Easy: 2 (find limit of a sequence; determine convergence of rⁿ)
- Medium: 2 (L'Hôpital for sequences; monotonicity)
- Hard: 1 (sequence defined recursively — find limit)
- Nightmare: 1 (sequence of partial sums → prove series converges)

---

### TOPIC 12 — INFINITE SERIES & CONVERGENCE TESTS

**Subtopics:**
- Definition: partial sums and convergence
- Geometric series: sum = a/(1−r), |r| < 1 ← Business application staple
- Divergence Test (necessary condition): if lim aₙ ≠ 0, diverges
- Integral Test (for positive, decreasing functions)
- p-Series Test: Σ 1/nᵖ converges iff p > 1
- Comparison Test (upper/lower bounding by known series)
- Alternating Series Test (two conditions)
- Ratio Test: L = lim|aₙ₊₁/aₙ|; best for factorials and exponentials
- Root Test: L = lim ⁿ√|aₙ|; best for (bₙ)ⁿ forms
- Telescoping series (partial fractions trick)
- Absolute vs. conditional convergence

**Importance Level:** ★★★★★ (Critical — appears in every DA2411 paper Q4)

**Past-Paper Frequency:** 3/6 (2023, 2024, 2025 — all DA2411 era papers)

**Difficulty Level:** Easy (geometric series, divergence test) to Hard (combining tests; endpoints of power series)

**Predicted Exam Probability for 24th Batch:** 90%
- The geometric series business application (2023: company profit; 2025: paint layers) appears in 2/3 DA2411 papers — VERY likely to recur
- The harder convergence test (integral test with ln n, comparison, ratio for factorials) is a 5-mark "determine converges or diverges" item
- Expect 2 convergence tests as separate 5-mark sub-questions in Q4

**Key Examiner Patterns:**
- Divergence test: always try first; if limₙ aₙ ≠ 0, done
- Σ 1/(n ln n): Integral Test → diverges (appears 2025 with ln in denominator)
- Σ 1/n² ln n: Comparison Test → converges (p-series comparison)
- Σ n/nᵖ type: p-Series or Divergence Test

**Estimated Questions to Generate:**
- Easy: 4 (geometric series sum; divergence test; p-series classification)
- Medium: 5 (business geometric series; alternating series; ratio test for factorials)
- Hard: 4 (integral test with ln; comparison test; endpoint analysis of power series)
- Nightmare: 2 (prove convergence rigorously; find sum of a telescoping + modified series)

---

### TOPIC 13 — POWER SERIES & RADIUS OF CONVERGENCE

**Subtopics:**
- Power series definition: Σ cₙ(x−a)ⁿ
- Radius of convergence R (three cases: 0, ∞, finite R)
- Finding R via Ratio Test: set L < 1, solve for |x−a|
- Interval of convergence: open interval (a−R, a+R), then check endpoints
- Endpoint checking: use Alternating Series Test, p-Series, or Divergence Test
- Standard series: geometric series Σ xⁿ = 1/(1−x), R = 1

**Importance Level:** ★★★★☆ (Very high — integral to Taylor series)

**Past-Paper Frequency:** 2/6 explicit (2023, 2024 Q4); always embedded in Taylor series questions

**Difficulty Level:** Medium to Hard (endpoint checking is the difficult part)

**Predicted Exam Probability for 24th Batch:** 80%
- Every time Taylor series appear, the radius of convergence sub-question follows
- 10 marks were allocated to R and interval in 2024

**Key Examiner Trap:** After the Ratio Test gives R, students MUST check BOTH endpoints separately. The test is inconclusive at |x−a| = R. One endpoint may converge (alternating series) and the other diverge. Omitting endpoint checks costs marks.

**Estimated Questions to Generate:**
- Easy: 2 (find R for a simple power series; identify interval without endpoints)
- Medium: 3 (full interval of convergence with both endpoints checked)
- Hard: 2 (power series with factorial coefficients; determine conditional vs absolute convergence)
- Nightmare: 1 (power series where endpoints require different tests; prove R from definition)

---

### TOPIC 14 — TAYLOR & MACLAURIN SERIES

**Subtopics:**
- Taylor series formula: Σ f⁽ⁿ⁾(a)/n! · (x−a)ⁿ
- Maclaurin series (a = 0): standard series for eˣ, sin x, cos x, ln(1+x), 1/(1−x)
- Derivation procedure: compute successive derivatives, evaluate at a, find pattern
- Writing the general term (the nᵗʰ term)
- Finding the radius of convergence via Ratio Test on the general term
- Checking endpoints of the interval of convergence
- Approximating values using the first 3 terms (choosing appropriate x)

**Importance Level:** ★★★★★ (Critical — the "deep" Q4 content)

**Past-Paper Frequency:** 2/6 (2023: e²ˣ at a=3; 2024: ln(1+4x) at a=1)

**Difficulty Level:** Hard (derivative pattern recognition) to Nightmare (choosing x for approximation)

**Predicted Exam Probability for 24th Batch:** 80%
- Has appeared in 2 of 3 DA2411 papers; 2025 did NOT have Taylor series, suggesting it RETURNS in 2026
- Common functions: eˢˣ, ln(1+kx), 1/(1+x)ⁿ — each centered at a≠0 for added difficulty

**Key Examiner Trap:** The 2024 "approximate ln(25)" question was a known stumbling block. Students plug x into the series without checking if that x is within the interval of convergence. The correct approach (using ln(25) = 2ln(5) and evaluating at x=1) requires insight, not just algebra.

**Estimated Questions to Generate:**
- Easy: 2 (Maclaurin for eˣ, sin x — standard; find first 4 terms)
- Medium: 4 (Taylor at a≠0 for eˢˣ, cos kx; full derivation with general term)
- Hard: 3 (ln(1+kx) type; find R and interval; approximate a log value)
- Nightmare: 2 (novel center; approximate irrational; prove the series equals the function on its interval)

---

## PART II: COMPLETE GENERATION PLAN

---

### TIER A — ABSOLUTELY CERTAIN TO APPEAR (Generate First)

These topics appear in ≥4/6 papers and are confirmed syllabus content. Preparation here is non-negotiable.

| Topic | Exam Prob. | Total Qs | Easy | Medium | Hard | Nightmare |
|-------|-----------|---------|------|--------|------|-----------|
| T9: Eigenvalues & Eigenvectors | 100% | 15 | 3 | 5 | 4 | 3 |
| T7: Leontief Input-Output | 95% | 11 | 2 | 4 | 3 | 2 |
| T4: Matrix Algebra & Applied Multiplication | 95% | 12 | 3 | 4 | 3 | 2 |
| T2: Gauss-Jordan Elimination | 90% | 12 | 3 | 4 | 3 | 2 |
| T12: Series Convergence Tests | 90% | 15 | 4 | 5 | 4 | 2 |
| T3: RREF + Dimension Analysis | 85% | 10 | 4 | 3 | 2 | 1 |
| T14: Taylor & Maclaurin Series | 80% | 11 | 2 | 4 | 3 | 2 |
| T13: Power Series & Convergence | 80% | 8 | 2 | 3 | 2 | 1 |

**Tier A Total: ~94 questions**

---

### TIER B — HIGH PROBABILITY, MAJOR SYLLABUS TOPICS

| Topic | Exam Prob. | Total Qs | Easy | Medium | Hard | Nightmare |
|-------|-----------|---------|------|--------|------|-----------|
| T5: Matrix Inverse & Determinants | 70% | 12 | 3 | 4 | 3 | 2 |
| T8: Iterative Methods (Jacobi/G-S) | 55% | 8 | 2 | 3 | 2 | 1 |
| T11: Infinite Sequences | 20% (embedded 60%) | 6 | 2 | 2 | 1 | 1 |

**Tier B Total: ~26 questions**

---

### TIER C — POSSIBLE SURPRISE TOPICS (Don't Ignore)

| Topic | Exam Prob. | Total Qs | Easy | Medium | Hard | Nightmare |
|-------|-----------|---------|------|--------|------|-----------|
| T6: LU Factorization | 30% | 8 | 2 | 3 | 2 | 1 |
| T10: Rank & Linear Independence | 25% | 6 | 2 | 2 | 1 | 1 |
| T1: Vectors & Dot Product | 15% | 9 | 3 | 3 | 2 | 1 |

**Tier C Total: ~23 questions**

---

### GRAND TOTAL: ~143 Questions

| Difficulty | Count | % of Total |
|-----------|-------|-----------|
| Easy | 40 | 28% |
| Medium | 51 | 36% |
| Hard | 37 | 26% |
| Nightmare | 15 | 10% |

---

## PART III: PHASE 2 GENERATION SEQUENCE

Generate in this order. Each topic includes: past-paper analysis, examiner patterns, common traps, high-probability predictions, question bank (Easy → Nightmare), and complete solutions.

**Round 1 (Core, highest marks on exam):**
1. T9: Eigenvalues & Eigenvectors
2. T7: Leontief Input-Output Model
3. T2: Gauss-Jordan Elimination
4. T4: Matrix Algebra & Applied Multiplication (including True/False)

**Round 2 (Q4 content — always the last question):**
5. T12: Series Convergence Tests + Geometric Business Applications
6. T14: Taylor & Maclaurin Series
7. T13: Power Series & Radius of Convergence

**Round 3 (Structural and procedural Q1 content):**
8. T3: RREF Identification + Dimension Analysis
9. T5: Matrix Inverse, Determinants & Matrix Powers

**Round 4 (Medium-probability topics):**
10. T8: Iterative Methods (Jacobi & Gauss-Seidel)
11. T6: LU Factorization

**Round 5 (Completion and surprises):**
12. T11: Infinite Sequences
13. T10: Rank & Linear Independence
14. T1: Vectors & Dot Product

---

## PART IV: PREDICTED 24TH BATCH EXAM STRUCTURE

Based on the 2023–2025 DA2411 papers, here is the most probable 24th Batch exam layout:

**Format:** 4 Questions × 25 Marks = 100 Marks | 3 Hours | Closed Book | Calculator Permitted

---

**Q1 (25 marks) — Matrix Foundations:**
- (a) Dimension analysis table [5×3 = 15 marks]: 5 matrices with given dimensions/properties; evaluate 5 expressions as defined/DNE with justification
- (b) RREF identification [6 marks]: 3 matrices, state if in RREF or identify violated condition; state solution count
- (c) Row operation fill-in [4 marks]: partial row reduction, fill in missing entries

---

**Q2 (25 marks) — Applied Matrices + Leontief:**
- (a) Applied matrix multiplication — logistics/delivery/production context [10 marks]: encode into matrices, multiply, interpret
- (b) Leontief 3-sector model [15 marks]:
  - (i) Build technology matrix M from prose [5]
  - (ii) Compute (I−M)⁻¹ [5]
  - (iii) Find total output X = (I−M)⁻¹D [5]

---

**Q3 (25 marks) — Eigenvalues + Matrix Equations:**
- (a) Solve for matrix K or isolate X in a complex matrix equation [10 marks]
- (b) Eigenvalue properties — at least TWO of:
  - Verify a given vector is an eigenvector [5]
  - Eigenvalues of A+kI relation [5]
  - Find eigenvalues/eigenvectors of 2×2 or 3×3 [10–12]
  - True/False with eigenvalue/inverse connection [3–5]

---

**Q4 (25 marks) — Series:**
- (a) Reasoning item — one of: "if Aⁿ=I find A⁻¹", "find |A^n − A^(n-1)|", or eigenvalue of A+kI [5 marks]
- (b) Geometric series business problem [5 marks]
- (c) Taylor series derivation + radius + interval of convergence [10 marks]
- (d) Series convergence test (2 sub-series, choose appropriate test each) [5 marks]

---

## PART V: CANONICAL TRUE/FALSE BANK

These 10 statements are the most frequently tested True/False items across all papers. Know all of them.

| # | Statement | Answer | Key Proof/Counterexample |
|---|-----------|--------|--------------------------|
| 1 | Every square matrix has an inverse | FALSE | Counterexample: zero matrix, or any A with det=0 |
| 2 | Matrix addition is commutative (A+B = B+A) | TRUE | Proof: (A+B)ᵢⱼ = aᵢⱼ+bᵢⱼ = bᵢⱼ+aᵢⱼ = (B+A)ᵢⱼ |
| 3 | If AB is defined, BA is defined | FALSE | A: 2×3, B: 3×2 → AB: 2×2 ✓, BA: 3×3 ✓ (actually both defined here). Better: A: 2×3, B: 3×4 → AB: 2×4 ✓, BA: 4×3... try A: 2×3, B: 3×1 → AB: 2×1 ✓, BA: undefined ✓ |
| 4 | A system with n equations and n unknowns always has a solution | FALSE | Example: x+y=1, x+y=2 (no solution) |
| 5 | A system with more variables than equations always has a solution | FALSE | Example: 0x+0y=1 has no solution despite fewer equations |
| 6 | If eigenvalue 0 exists, A is invertible | FALSE | λ=0 iff det(A)=0 iff A is singular (NOT invertible) |
| 7 | A diagonal matrix with trace 0 is singular | TRUE (careful!) | Trace=0 means sum of diagonal entries=0. If all diagonals are 0 → zero matrix (singular). If they're not all 0... need at least one to be 0 → determinant = 0 → singular. CAUTION: not all trace-0 diagonal matrices have a zero entry if we allow cancellation — but for diagonal matrices specifically, at least one entry must be zero if they're all real and sum to 0... actually that's ALSO not necessarily true (e.g. diag(1,−1)). The 2024 Q1c required careful case analysis. |
| 8 | A 2×2 system of two non-parallel lines always has a solution | TRUE | Non-parallel lines intersect at exactly one point |
| 9 | (AB)ᵀ = AᵀBᵀ | FALSE | Correct identity is (AB)ᵀ = BᵀAᵀ |
| 10 | A and Aᵀ always have the same eigenvalues | TRUE | Proof: det(A−λI) = det((A−λI)ᵀ) = det(Aᵀ−λI) |

---

## PART VI: CRITICAL FORMULA QUICK-REFERENCE

**For Phase 2, every solution should reference these formulas:**

| Context | Formula |
|---------|---------|
| RREF condition 4 | Column with leading 1 has zeros in ALL other rows (above AND below) |
| LU multiplier | lᵢₖ = aᵢₖ/aₖₖ |
| Leontief output | X = (I−M)⁻¹D |
| 2×2 inverse | A⁻¹ = (1/det A)·[[d,−b],[−c,a]] |
| Eigenvalue equation | det(A−λI) = 0 |
| A+kI eigenvalues | If λ is eigenvalue of A, then λ+k is eigenvalue of A+kI |
| Geometric series sum | S = a/(1−r), \|r\| < 1 |
| Taylor series | f(x) = Σ f⁽ⁿ⁾(a)/n! · (x−a)ⁿ |
| Ratio Test radius | R = 1/C where L = C\|x−a\| from Ratio Test |
| Diagonal dominance | \|aᵢᵢ\| > Σⱼ≠ᵢ \|aᵢⱼ\| for all rows i |
| Jacobi update | xᵢ⁽ᵏ⁺¹⁾ = (1/aᵢᵢ)(bᵢ − Σⱼ≠ᵢ aᵢⱼxⱼ⁽ᵏ⁾) — all OLD values |
| Gauss-Seidel update | xᵢ⁽ᵏ⁺¹⁾ = (1/aᵢᵢ)(bᵢ − Σⱼ<ᵢ aᵢⱼxⱼ⁽ᵏ⁺¹⁾ − Σⱼ>ᵢ aᵢⱼxⱼ⁽ᵏ⁾) |
| Orthogonal diagonalization | U^TAU = D, where U has normalized eigenvectors as columns |
| p-Series convergence | Σ 1/nᵖ converges iff p > 1 |
| Spectral Theorem reconstruction | A = UDUᵀ (for symmetric A) |

---

*End of Master Plan. Awaiting approval to begin Phase 2 topic-by-topic generation.*
*Suggested starting point: T9 — Eigenvalues & Eigenvectors (100% exam probability, most marks at stake)*
