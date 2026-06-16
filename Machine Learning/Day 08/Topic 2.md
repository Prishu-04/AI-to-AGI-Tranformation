# Matrix Terminology and Structure
## 1. Goals
```
- Read standard matrix notation confidently.
- Identify rows, columns, entries, dimensions and shapes.
- Distinguish square, rectangular, diagonal, identity, zero, triangular and symmetric matrices.
- Calculate and interpret the transpose and trace.
- Understand determinant, rank and inverse intuitively.
- Connect matrices to systems of linear equations.
- Create and inspect different matrix structures using NumPy.
```
---
## 2. Why Matrix Structure Matters
A matrix is not merely a table of numbers. Its structure tells us what mathematical operations are possible and what information the matrix contains.
Consider a dataset:
![[Pasted image 20260616112926.png|237]]
A matrix is not merely a table of numbers. Its structure tells us what mathematical operations are possible and what information the matrix contains.

Consider a dataset:

X=[685724706589281]X= \begin{bmatrix} 6 & 85 & 72\\ 4 & 70 & 65\\ 8 & 92 & 81 \end{bmatrix}X=​648​857092​726581​​

It could represent:

- Three students
- Three features per student
- Rows as observations
- Columns as features

Now consider a neural-network weight matrix:

W=[0.2−0.50.70.1−0.30.8]W= \begin{bmatrix} 0.2 & -0.5\\ 0.7 & 0.1\\ -0.3 & 0.8 \end{bmatrix}W=​0.20.7−0.3​−0.50.10.8​​

This matrix does not represent a dataset. It represents a transformation from three input features to two output units.

The matrix’s meaning depends on:

- Its shape
- The meaning assigned to rows and columns
- Its internal structure
- The operation in which it is used

---

# 3. Industry applications

## Neural networks

Every dense neural-network layer contains a weight matrix:

Z=XW+bZ=XW+bZ=XW+b

The shape of WWW determines:

- How many inputs the layer accepts
- How many outputs it generates
- How many trainable parameters it contains

## Recommendation systems

A user-item interaction matrix may look like:

R=[504030450]R= \begin{bmatrix} 5 & 0 & 4\\ 0 & 3 & 0\\ 4 & 5 & 0 \end{bmatrix}R=​504​035​400​​

Rows may represent users, while columns represent products, songs or movies.

## Computer vision

Matrices represent:

- Grayscale images
- Convolution filters
- Geometric transformations
- Feature maps
- Attention maps

## Natural language processing

Matrices are used for:

- Token embeddings
- Attention scores
- Query, key and value transformations
- Vocabulary projections
- Batches of hidden representations

## Financial and scientific systems

Matrices can represent:

- Asset covariance
- Customer transactions
- Sensor readings
- Physical transformations
- Linear constraints
- Risk relationships

Major AI systems built by organisations such as Google, Microsoft, Meta, NVIDIA, Amazon, Netflix and OpenAI depend heavily on matrix and tensor operations.

---

# 4. Interview relevance

Common interview questions include:

- What is the shape of a matrix?
- What is a square matrix?
- What is the identity matrix?
- What does transposing a matrix do?
- What is matrix rank?
- When does a matrix have an inverse?
- What is a singular matrix?
- What is the difference between an identity matrix and a zero matrix?
- Why does matrix rank matter in machine learning?
- What does the determinant indicate?
- Why can highly correlated features create matrix problems?

Production-oriented interviews may ask:

- How would you validate matrix inputs?
- Why can a matrix operation consume excessive memory?
- How do you detect a rank-deficient feature matrix?
- Why should you avoid explicitly computing matrix inverses?
- How do sparse matrices reduce memory usage?

---

# 5. Basic matrix notation

A general matrix with mmm rows and nnn columns is written as:

A=[a11a12⋯a1na21a22⋯a2n⋮⋮⋱⋮am1am2⋯amn]A= \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n}\\ a_{21} & a_{22} & \cdots & a_{2n}\\ \vdots & \vdots & \ddots & \vdots\\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}A=​a11​a21​⋮am1​​a12​a22​⋮am2​​⋯⋯⋱⋯​a1n​a2n​⋮amn​​​

We write:

A∈Rm×nA\in\mathbb{R}^{m\times n}A∈Rm×n

This means:

- AAA contains real numbers.
- AAA has mmm rows.
- AAA has nnn columns.

---

## Example

A=[246135]A= \begin{bmatrix} 2 & 4 & 6\\ 1 & 3 & 5 \end{bmatrix}A=[21​43​65​]

It has:

- 2 rows
- 3 columns
- Shape 2×32\times32×3
- 6 total entries

Therefore:

A∈R2×3A\in\mathbb{R}^{2\times3}A∈R2×3

---

# 6. Matrix entries

The notation aija_{ij}aij​ means:

- iii: row number
- jjj: column number

For:

A=[246135]A= \begin{bmatrix} 2 & 4 & 6\\ 1 & 3 & 5 \end{bmatrix}A=[21​43​65​]

we have:

a11=2a_{11}=2a11​=2 a13=6a_{13}=6a13​=6 a21=1a_{21}=1a21​=1 a23=5a_{23}=5a23​=5

## Important difference from Python

Mathematical indexing usually starts from 1.

Python indexing starts from 0.

Therefore:

a23a_{23}a23​

corresponds to:

```
A[1, 2]
```

---

## NumPy implementation

```
import numpy as npA = np.array([    [2, 4, 6],    [1, 3, 5]], dtype=np.float64)print("Matrix:")print(A)print("Shape:", A.shape)print("Rows:", A.shape[0])print("Columns:", A.shape[1])print("Total entries:", A.size)print("Mathematical a_23:", A[1, 2])
```

---

# 7. Rows and columns

For:

A=[246135]A= \begin{bmatrix} 2 & 4 & 6\\ 1 & 3 & 5 \end{bmatrix}A=[21​43​65​]

the first row is:

[246]\begin{bmatrix} 2 & 4 & 6 \end{bmatrix}[2​4​6​]

The second column is:

[43]\begin{bmatrix} 4\\ 3 \end{bmatrix}[43​]

## NumPy

```
first_row = A[0, :]second_column = A[:, 1]print("First row:", first_row)print("Second column:", second_column)
```

Output:

```
First row: [2. 4. 6.]Second column: [4. 3.]
```

Notice that both results have shape `(3,)` or `(2,)`, not explicit row or column shapes.

To preserve two-dimensional structure:

```
first_row_2d = A[0:1, :]second_column_2d = A[:, 1:2]print(first_row_2d.shape)print(second_column_2d.shape)
```

Output:

```
(1, 3)(2, 1)
```

This difference becomes important during matrix multiplication.

---

# 8. Types of matrices

## 8.1 Rectangular matrix

A rectangular matrix has a different number of rows and columns.

A=[123456]A= \begin{bmatrix} 1 & 2 & 3\\ 4 & 5 & 6 \end{bmatrix}A=[14​25​36​]

Shape:

2×32\times32×3

Most ML datasets are rectangular because the number of observations is usually different from the number of features.

```
A = np.array([    [1, 2, 3],    [4, 5, 6]])print(A.shape)
```

---

## 8.2 Square matrix

A square matrix has the same number of rows and columns.

A=[1234]A= \begin{bmatrix} 1 & 2\\ 3 & 4 \end{bmatrix}A=[13​24​]

Shape:

2×22\times22×2

Square matrices appear in:

- Covariance matrices
- Correlation matrices
- Transformation matrices
- Hessian matrices
- Attention-score matrices
- Systems of equations

```
A = np.array([    [1, 2],    [3, 4]])is_square = A.shape[0] == A.shape[1]print("Square matrix:", is_square)
```

---

## 8.3 Row matrix

A row matrix contains exactly one row.

R=[258]R= \begin{bmatrix} 2 & 5 & 8 \end{bmatrix}R=[2​5​8​]

Shape:

1×31\times31×3

```
R = np.array([[2, 5, 8]])print(R.shape)
```

Output:

```
(1, 3)
```

---

## 8.4 Column matrix

A column matrix contains exactly one column.

C=[258]C= \begin{bmatrix} 2\\ 5\\ 8 \end{bmatrix}C=​258​​

Shape:

3×13\times13×1

```
C = np.array([    [2],    [5],    [8]])print(C.shape)
```

Output:

```
(3, 1)
```

---

## 8.5 Zero matrix

A zero matrix contains only zeros.

O=[0000]O= \begin{bmatrix} 0 & 0\\ 0 & 0 \end{bmatrix}O=[00​00​]

The zero matrix behaves like zero in ordinary addition:

A+O=AA+O=AA+O=A

```
O = np.zeros((2, 3))print(O)
```

### ML applications

Zero matrices may be used for:

- Initial placeholders
- Masks
- Gradient buffers
- Padding
- Empty accumulators

However, initializing all neural-network weights to zero can prevent neurons from learning different features because of symmetry.

---

## 8.6 Ones matrix

A ones matrix contains only ones.

J=[1111]J= \begin{bmatrix} 1 & 1\\ 1 & 1 \end{bmatrix}J=[11​11​]

```
J = np.ones((2, 3))print(J)
```

Applications include:

- Masks
- Baseline arrays
- Initialisation experiments
- Broadcasting demonstrations

---

# 9. Diagonal matrices

A diagonal matrix is a square matrix where all off-diagonal entries are zero.

D=[300050007]D= \begin{bmatrix} 3 & 0 & 0\\ 0 & 5 & 0\\ 0 & 0 & 7 \end{bmatrix}D=​300​050​007​​

The main diagonal is:

[3,5,7][3,5,7][3,5,7]

## Why diagonal matrices are useful

Multiplying by a diagonal matrix independently scales different dimensions.

For example:

- First feature multiplied by 3
- Second feature multiplied by 5
- Third feature multiplied by 7

Diagonal matrices appear in:

- Feature scaling
- Eigenvalue decomposition
- Covariance approximations
- Regularisation
- Optimisation
- Variance representation

## NumPy

```
values = np.array([3, 5, 7])D = np.diag(values)print(D)print("Diagonal:", np.diag(D))
```

---

## Checking whether a matrix is diagonal

```
def is_diagonal(matrix: np.ndarray) -> bool:    if matrix.ndim != 2:        return False    if matrix.shape[0] != matrix.shape[1]:        return False    diagonal_part = np.diag(np.diag(matrix))    return np.array_equal(matrix, diagonal_part)D = np.array([    [3, 0, 0],    [0, 5, 0],    [0, 0, 7]])print(is_diagonal(D))
```

---

# 10. Identity matrix

An identity matrix is a diagonal matrix containing ones along the main diagonal.

I3=[100010001]I_3= \begin{bmatrix} 1 & 0 & 0\\ 0 & 1 & 0\\ 0 & 0 & 1 \end{bmatrix}I3​=​100​010​001​​

The identity matrix behaves like the number 1 in multiplication:

AI=AAI=AAI=A

and:

IA=AIA=AIA=A

provided the shapes are compatible.

## Intuition

The identity matrix performs no transformation.

If a vector enters an identity transformation, it leaves unchanged.

```
I = np.eye(3)print(I)
```

### ML applications

Identity matrices appear in:

- Regularisation
- Numerical stabilisation
- Residual connections
- Covariance calculations
- Initial transformations
- Matrix inverse formulas

For example, ridge regression uses a term related to:

XTX+λIX^TX+\lambda IXTX+λI

The identity matrix adds regularisation independently to model parameters.

---

# 11. Scalar matrix

A scalar matrix is an identity matrix multiplied by a scalar.

S=4I=[400040004]S=4I= \begin{bmatrix} 4 & 0 & 0\\ 0 & 4 & 0\\ 0 & 0 & 4 \end{bmatrix}S=4I=​400​040​004​​

```
S = 4 * np.eye(3)print(S)
```

It scales every coordinate equally.

---

# 12. Triangular matrices

## Upper triangular matrix

All entries below the main diagonal are zero.

U=[246035007]U= \begin{bmatrix} 2 & 4 & 6\\ 0 & 3 & 5\\ 0 & 0 & 7 \end{bmatrix}U=​200​430​657​​

```
U = np.array([    [2, 4, 6],    [0, 3, 5],    [0, 0, 7]])print(np.triu(U))
```

## Lower triangular matrix

All entries above the main diagonal are zero.

L=[200430657]L= \begin{bmatrix} 2 & 0 & 0\\ 4 & 3 & 0\\ 6 & 5 & 7 \end{bmatrix}L=​246​035​007​​

```
L = np.array([    [2, 0, 0],    [4, 3, 0],    [6, 5, 7]])print(np.tril(L))
```

### Why triangular matrices matter

They appear in:

- Gaussian elimination
- Solving linear systems
- LU decomposition
- Cholesky decomposition
- Numerical optimisation

Triangular systems are usually easier and faster to solve than general systems.

---

# 13. Matrix transpose

The transpose swaps rows and columns.

If:

A=[123456]A= \begin{bmatrix} 1 & 2 & 3\\ 4 & 5 & 6 \end{bmatrix}A=[14​25​36​]

then:

AT=[142536]A^T= \begin{bmatrix} 1 & 4\\ 2 & 5\\ 3 & 6 \end{bmatrix}AT=​123​456​​

Shape transformation:

2×3⟶3×22\times3 \longrightarrow 3\times22×3⟶3×2

## Entry definition

(AT)ij=Aji(A^T)_{ij}=A_{ji}(AT)ij​=Aji​

## NumPy

```
A = np.array([    [1, 2, 3],    [4, 5, 6]])A_transpose = A.Tprint("Original:")print(A)print("Shape:", A.shape)print("\nTranspose:")print(A_transpose)print("Shape:", A_transpose.shape)
```

---

## Critical NumPy trap

```
x = np.array([1, 2, 3])print(x.shape)print(x.T.shape)
```

Output:

```
(3,)(3,)
```

The transpose does not change a one-dimensional array.

To create a column vector:

```
x_column = x.reshape(-1, 1)print(x_column)print(x_column.shape)
```

Output:

```
[[1] [2] [3]](3, 1)
```

To create a row vector:

```
x_row = x.reshape(1, -1)print(x_row.shape)
```

Output:

```
(1, 3)
```

---

# 14. Transpose properties

For compatible matrices:

(AT)T=A(A^T)^T=A(AT)T=A (A+B)T=AT+BT(A+B)^T=A^T+B^T(A+B)T=AT+BT (cA)T=cAT(cA)^T=cA^T(cA)T=cAT

The most important multiplication property is:

(AB)T=BTAT(AB)^T=B^TA^T(AB)T=BTAT

Notice that the order reverses.

This will become important in matrix multiplication and gradient derivations.

---

# 15. Symmetric matrix

A square matrix is symmetric when:

A=ATA=A^TA=AT

Example:

A=[241435157]A= \begin{bmatrix} 2 & 4 & 1\\ 4 & 3 & 5\\ 1 & 5 & 7 \end{bmatrix}A=​241​435​157​​

The values mirror across the main diagonal.

## NumPy check

```
A = np.array([    [2.0, 4.0, 1.0],    [4.0, 3.0, 5.0],    [1.0, 5.0, 7.0]])print(np.allclose(A, A.T))
```

Use `np.allclose()` rather than exact equality when working with floating-point calculations.

### ML importance

These matrices are often symmetric:

- Covariance matrices
- Correlation matrices
- Hessian matrices
- Gram matrices
- Kernel matrices

Symmetric matrices have useful mathematical properties that will matter when studying eigenvalues, eigenvectors and PCA.

---

# 16. Main diagonal and trace

For:

A=[241435157]A= \begin{bmatrix} 2 & 4 & 1\\ 4 & 3 & 5\\ 1 & 5 & 7 \end{bmatrix}A=​241​435​157​​

the main diagonal is:

[2,3,7][2,3,7][2,3,7]

The trace is the sum of diagonal entries:

tr⁡(A)=2+3+7=12\operatorname{tr}(A)=2+3+7=12tr(A)=2+3+7=12

## NumPy

```
diagonal = np.diag(A)trace = np.trace(A)print("Diagonal:", diagonal)print("Trace:", trace)
```

### ML significance

For a covariance matrix, the trace equals the total variance across its diagonal features.

Trace also appears in:

- Matrix calculus
- Optimisation objectives
- Statistical estimation
- Regularisation
- Dimensionality reduction

---

# 17. Determinant intuition

The determinant is a scalar associated with a square matrix.

For a 2×22\times22×2 matrix:

A=[abcd]A= \begin{bmatrix} a & b\\ c & d \end{bmatrix}A=[ac​bd​]

the determinant is:

det⁡(A)=ad−bc\det(A)=ad-bcdet(A)=ad−bc

Example:

A=[2134]A= \begin{bmatrix} 2 & 1\\ 3 & 4 \end{bmatrix}A=[23​14​] det⁡(A)=(2)(4)−(1)(3)=5\det(A)=(2)(4)-(1)(3)=5det(A)=(2)(4)−(1)(3)=5

## Geometric intuition

A matrix transforms space.

The absolute determinant tells us how much the transformation scales area or volume.

- ∣det⁡(A)∣>1|\det(A)|>1∣det(A)∣>1: space expands.
- 0<∣det⁡(A)∣<10<|\det(A)|<10<∣det(A)∣<1: space contracts.
- det⁡(A)<0\det(A)<0det(A)<0: orientation flips.
- det⁡(A)=0\det(A)=0det(A)=0: space collapses into a lower dimension.

When:

det⁡(A)=0\det(A)=0det(A)=0

the matrix is singular and has no inverse.

## NumPy

```
A = np.array([    [2.0, 1.0],    [3.0, 4.0]])determinant = np.linalg.det(A)print("Determinant:", determinant)
```

Because of floating-point calculations, you may see:

```
4.999999999999999
```

instead of exactly `5`.

---

# 18. Matrix rank intuition

Rank tells us how many independent directions or independent pieces of information a matrix contains.

Consider:

A=[1224]A= \begin{bmatrix} 1 & 2\\ 2 & 4 \end{bmatrix}A=[12​24​]

The second row is twice the first row.

Therefore, the second row does not provide new independent information.

The matrix has rank 1, not rank 2.

```
A = np.array([    [1.0, 2.0],    [2.0, 4.0]])print("Rank:", np.linalg.matrix_rank(A))
```

---

## Full rank

For an m×nm\times nm×n matrix, the maximum possible rank is:

min⁡(m,n)\min(m,n)min(m,n)

A matrix is full rank when:

rank⁡(A)=min⁡(m,n)\operatorname{rank}(A)=\min(m,n)rank(A)=min(m,n)

Example:

```
A = np.array([    [1.0, 2.0],    [3.0, 4.0]])print(np.linalg.matrix_rank(A))
```

Output:

```
2
```

---

## Why rank matters in ML

Suppose two dataset features are identical:

```
monthly_salaryannual_salary / 12
```

These columns may contain the same information.

This can cause:

- Redundant features
- Unstable coefficient estimates
- Singular matrices
- Multicollinearity
- Unnecessary memory and computation
- Poor interpretability

Rank helps reveal whether matrix dimensions truly contain independent information.

---

# 19. Inverse matrix intuition

For a nonzero scalar aaa:

a⋅1a=1a\cdot\frac{1}{a}=1a⋅a1​=1

For a square matrix AAA, its inverse A−1A^{-1}A−1 satisfies:

AA−1=IAA^{-1}=IAA−1=I

and:

A−1A=IA^{-1}A=IA−1A=I

## Example

A=[2004]A= \begin{bmatrix} 2 & 0\\ 0 & 4 \end{bmatrix}A=[20​04​]

Then:

A−1=[120014]A^{-1}= \begin{bmatrix} \frac12 & 0\\ 0 & \frac14 \end{bmatrix}A−1=[21​0​041​​]

because:

AA−1=IAA^{-1}=IAA−1=I

## NumPy

```
A = np.array([    [2.0, 0.0],    [0.0, 4.0]])A_inverse = np.linalg.inv(A)print(A_inverse)print(A @ A_inverse)
```

---

## When does an inverse exist?

A matrix must generally be:

1. Square
2. Full rank
3. Non-singular
4. Have a nonzero determinant

For a square matrix:

det⁡(A)≠0\det(A)\neq0det(A)=0

is required for an inverse.

---

## Production engineering warning

Do not usually solve a linear system by explicitly calculating:

```
x = np.linalg.inv(A) @ b
```

Prefer:

```
x = np.linalg.solve(A, b)
```

Why?

- More numerically stable
- Usually faster
- Avoids unnecessary inverse construction
- Uses specialised numerical methods

---

# 20. Singular matrix

A singular matrix has no inverse.

Example:

A=[1224]A= \begin{bmatrix} 1 & 2\\ 2 & 4 \end{bmatrix}A=[12​24​]

Its determinant is:

(1)(4)−(2)(2)=0(1)(4)-(2)(2)=0(1)(4)−(2)(2)=0

Its rows are dependent.

Trying to invert it:

```
A = np.array([    [1.0, 2.0],    [2.0, 4.0]])inverse = np.linalg.inv(A)
```

Likely error:

```
numpy.linalg.LinAlgError: Singular matrix
```

### Root cause

The matrix has collapsed information into fewer independent dimensions.

### ML causes

- Duplicate features
- Perfectly correlated columns
- Insufficient observations
- Incorrect feature engineering
- One-hot encoding all categories with an intercept
- Numerical precision problems

---

# 21. Matrix as a linear transformation

A matrix can transform a vector.

Suppose:

A=[2003]A= \begin{bmatrix} 2 & 0\\ 0 & 3 \end{bmatrix}A=[20​03​]

and:

x=[12]\mathbf{x}= \begin{bmatrix} 1\\ 2 \end{bmatrix}x=[12​]

Then:

Ax=[26]A\mathbf{x}= \begin{bmatrix} 2\\ 6 \end{bmatrix}Ax=[26​]

The matrix scales:

- The first coordinate by 2
- The second coordinate by 3

Matrices can perform:

- Scaling
- Rotation
- Reflection
- Projection
- Shearing
- Feature mixing
- Dimension transformation

A neural-network weight matrix is also a learned transformation.

---

# 22. Systems of linear equations

Consider:

2x+y=52x+y=52x+y=5 x−y=1x-y=1x−y=1

This can be represented as:

[211−1][xy]=[51]\begin{bmatrix} 2 & 1\\ 1 & -1 \end{bmatrix} \begin{bmatrix} x\\ y \end{bmatrix} = \begin{bmatrix} 5\\ 1 \end{bmatrix}[21​1−1​][xy​]=[51​]

Compact form:

Ax=bA\mathbf{x}=\mathbf{b}Ax=b

where:

A=[211−1]A= \begin{bmatrix} 2 & 1\\ 1 & -1 \end{bmatrix}A=[21​1−1​] x=[xy]\mathbf{x}= \begin{bmatrix} x\\ y \end{bmatrix}x=[xy​] b=[51]\mathbf{b}= \begin{bmatrix} 5\\ 1 \end{bmatrix}b=[51​]

## NumPy solution

```
A = np.array([    [2.0, 1.0],    [1.0, -1.0]])b = np.array([5.0, 1.0])solution = np.linalg.solve(A, b)print("x:", solution[0])print("y:", solution[1])
```

Output:

```
x: 2.0y: 1.0
```

Verification:

```
print(A @ solution)print(b)
```

Both should be approximately equal.

---

# 23. Design matrix in machine learning

A feature matrix is often called a **design matrix**.

Suppose:

X=[685724706589281]X= \begin{bmatrix} 6 & 85 & 72\\ 4 & 70 & 65\\ 8 & 92 & 81 \end{bmatrix}X=​648​857092​726581​​

Rows represent students and columns represent features.

To include a bias or intercept term, a column of ones may be added:

Xbias=[168572147065189281]X_{\text{bias}}= \begin{bmatrix} 1 & 6 & 85 & 72\\ 1 & 4 & 70 & 65\\ 1 & 8 & 92 & 81 \end{bmatrix}Xbias​=​111​648​857092​726581​​

## NumPy

```
X = np.array([    [6.0, 85.0, 72.0],    [4.0, 70.0, 65.0],    [8.0, 92.0, 81.0]])ones = np.ones((X.shape[0], 1))X_with_bias = np.hstack((ones, X))print(X_with_bias)print(X_with_bias.shape)
```

The new shape becomes:

```
(3, 4)
```

---

# 24. Coding laboratory: matrix inspector

```
from __future__ import annotationsimport numpy as npfrom numpy.typing import NDArraydef inspect_matrix(matrix: NDArray[np.float64]) -> dict[str, object]:    if not isinstance(matrix, np.ndarray):        raise TypeError("matrix must be a NumPy array.")    if matrix.ndim != 2:        raise ValueError(            f"Expected a 2D matrix, received shape {matrix.shape}."        )    rows, columns = matrix.shape    is_square = rows == columns    report: dict[str, object] = {        "shape": matrix.shape,        "rows": rows,        "columns": columns,        "size": matrix.size,        "dtype": str(matrix.dtype),        "is_square": is_square,        "rank": int(np.linalg.matrix_rank(matrix)),        "contains_nan": bool(np.isnan(matrix).any()),        "contains_infinity": bool(np.isinf(matrix).any())    }    if is_square:        report["trace"] = float(np.trace(matrix))        report["determinant"] = float(np.linalg.det(matrix))        report["is_symmetric"] = bool(            np.allclose(matrix, matrix.T)        )        report["is_diagonal"] = bool(            np.allclose(matrix, np.diag(np.diag(matrix)))        )    return reportA = np.array([    [2.0, 1.0],    [1.0, 3.0]])report = inspect_matrix(A)for key, value in report.items():    print(f"{key}: {value}")
```

---

# 25. Safer structural checks

Floating-point calculations are rarely exact.

Avoid:

```
A == A.T
```

Prefer:

```
np.allclose(A, A.T)
```

Avoid:

```
np.linalg.det(A) == 0
```

Prefer a tolerance-based check:

```
determinant = np.linalg.det(A)is_nearly_singular = np.isclose(determinant, 0.0)
```

However, determinant alone is not always the most reliable numerical diagnostic. Condition numbers and singular values are often more informative.

---

# 26. Condition-number awareness

A matrix can technically be invertible but still be nearly singular.

Such a matrix is called **ill-conditioned**.

Small input changes may produce large output changes.

```
A = np.array([    [1.0, 1.0],    [1.0, 1.000001]])condition_number = np.linalg.cond(A)print("Condition number:", condition_number)
```

A large condition number suggests numerical instability.

## ML relevance

Poor conditioning can result from:

- Features with drastically different scales
- Strongly correlated features
- Duplicate information
- Bad numerical precision
- Poorly designed optimisation problems

Feature scaling can often improve conditioning and gradient-descent performance.

---

# 27. Sparse versus dense matrices

A dense matrix stores every entry, including zeros.

A sparse matrix stores mainly nonzero values and their locations.

Example:

X=[005003001000]X= \begin{bmatrix} 0 & 0 & 5 & 0\\ 0 & 3 & 0 & 0\\ 1 & 0 & 0 & 0 \end{bmatrix}X=​001​030​500​000​​

This matrix contains mostly zeros.

Sparse matrices are common in:

- Text data
- Bag-of-words representations
- Recommendation systems
- Graphs
- One-hot encoded data
- Large interaction matrices

Storing a huge sparse matrix as dense data can waste substantial memory.

Example using SciPy:

```
from scipy.sparse import csr_matrixdense_matrix = np.array([    [0, 0, 5, 0],    [0, 3, 0, 0],    [1, 0, 0, 0]])sparse_matrix = csr_matrix(dense_matrix)print(sparse_matrix)
```

---

# 28. Debugging laboratory

## Bug 1: Transposing a one-dimensional vector

Broken assumption:

```
x = np.array([1, 2, 3])x_transpose = x.Tprint(x_transpose.shape)
```

Output:

```
(3,)
```

### Root cause

A one-dimensional array has no explicit row or column axis to swap.

### Correction

```
x_column = x.reshape(-1, 1)x_row = x_column.Tprint(x_column.shape)print(x_row.shape)
```

---

## Bug 2: Inverting a rectangular matrix

Broken code:

```
A = np.array([    [1.0, 2.0, 3.0],    [4.0, 5.0, 6.0]])np.linalg.inv(A)
```

Likely error:

```
numpy.linalg.LinAlgError: Last 2 dimensions of the array must be square
```

### Root cause

The standard inverse is defined for square matrices.

### Possible alternatives

Depending on the problem:

- Solve a least-squares system.
- Use a pseudoinverse.
- Redesign the equation.

```
A_pseudoinverse = np.linalg.pinv(A)
```

The pseudoinverse is not identical to an ordinary inverse.

---

## Bug 3: Singular matrix

```
A = np.array([    [1.0, 2.0],    [2.0, 4.0]])np.linalg.inv(A)
```

Error:

```
numpy.linalg.LinAlgError: Singular matrix
```

### Correction strategy

Do not simply add random noise.

Investigate:

```
print("Rank:", np.linalg.matrix_rank(A))print("Determinant:", np.linalg.det(A))print("Condition number:", np.linalg.cond(A))
```

Then check for:

- Duplicate rows
- Duplicate features
- Perfect correlations
- Incorrect preprocessing

---

## Bug 4: Exact floating-point equality

Broken code:

```
result = A @ np.linalg.inv(A)print(result == np.eye(A.shape[0]))
```

Some values may unexpectedly be `False`.

### Root cause

Floating-point calculations contain small approximation errors.

### Correction

```
print(np.allclose(result, np.eye(A.shape[0])))
```

---

## Bug 5: Incorrect feature orientation

Expected:

```
100 observations × 5 features
```

Received:

```
5 observations × 100 features
```

The code may run until it reaches a model that expects five features.

### Detection

```
expected_features = 5if X.shape[1] != expected_features:    raise ValueError(        f"Expected {expected_features} features, "        f"received shape {X.shape}."    )
```

---

# 29. Top 10 common errors

1. Confusing mathematical indexing with Python indexing.
2. Treating a `(d,)` array as an explicit column vector.
3. Forgetting that transpose reverses matrix shape.
4. Attempting to invert a non-square matrix.
5. Attempting to invert a singular matrix.
6. Assuming a nonzero determinant guarantees good numerical stability.
7. Comparing floating-point matrices using exact equality.
8. Confusing rank with the number of rows or columns.
9. Storing a highly sparse dataset as a dense matrix.
10. Explicitly calculating an inverse when `solve()` is sufficient.

---

# 30. How senior engineers approach matrix problems

Before running an operation, they inspect:

```
print("Shape:", A.shape)print("Dimensions:", A.ndim)print("Datatype:", A.dtype)print("Finite:", np.isfinite(A).all())print("Rank:", np.linalg.matrix_rank(A))
```

For square matrices, they may also inspect:

```
print("Determinant:", np.linalg.det(A))print("Condition number:", np.linalg.cond(A))print("Symmetric:", np.allclose(A, A.T))
```

They then ask:

- What do the rows represent?
- What do the columns represent?
- Are the units compatible?
- Are any features redundant?
- Is the matrix sparse?
- Is inversion really necessary?
- Is the operation numerically stable?
- What should the output shape be?

---

# 31. Knowledge checkpoint

Answer these without looking back.

### Question 1

What is the shape of this matrix?

[123456]\begin{bmatrix} 1 & 2 & 3\\ 4 & 5 & 6 \end{bmatrix}[14​25​36​]

### Question 2

What is the transpose shape of a 7×47\times47×4 matrix?

### Question 3

What is special about an identity matrix?

### Question 4

What condition must a matrix satisfy to be symmetric?

### Question 5

What does matrix rank measure intuitively?

### Question 6

Why does a singular matrix have no inverse?

### Question 7

What is wrong with this code?

```
x = np.array([1, 2, 3])print(x.T.shape)
```

Nothing is syntactically wrong, but what misconception might occur?

### Question 8

Why is this usually discouraged?

```
x = np.linalg.inv(A) @ b
```

---

## Answers

1. 2×32\times32×3
2. 4×74\times74×7
3. It has ones on the main diagonal, zeros elsewhere, and leaves compatible vectors or matrices unchanged under multiplication.
4. It must be square and satisfy A=ATA=A^TA=AT.
5. The number of independent directions or independent information dimensions.
6. It collapses at least one direction, so the original input cannot be uniquely recovered.
7. A one-dimensional NumPy array does not change shape under transpose.
8. `np.linalg.solve(A, b)` is usually faster and more numerically stable.

---

# 32. Interview questions

## Beginner

1. What is a matrix entry?
2. What does A∈Rm×nA\in\mathbb{R}^{m\times n}A∈Rm×n mean?
3. What is a square matrix?
4. What is a diagonal matrix?
5. What is an identity matrix?
6. What does matrix transpose do?

## Intermediate

7. What is a symmetric matrix?
8. What does the determinant represent geometrically?
9. What does rank tell us?
10. What is a singular matrix?
11. When does a square matrix have an inverse?
12. Why can duplicate features cause rank deficiency?

## Advanced interview traps

### Trap 1

**Does every square matrix have an inverse?**

No. It must also be full rank or non-singular.

### Trap 2

**If the determinant is very small but nonzero, is inversion safe?**

Not necessarily. The matrix may be ill-conditioned.

### Trap 3

**Is `x.T` always a column vector?**

No. For a one-dimensional NumPy array, `.T` does not change its shape.

### Trap 4

**Does a high-dimensional matrix always have high rank?**

No. Its rows or columns may contain redundant information.

### Trap 5

**Should you compute an inverse to solve every linear system?**

No. Use a linear-system solver when possible.

---

# 33. Slot cheat sheet

```
Matrix shape(rows, columns)Square matrixrows == columnsDiagonal matrixoff-diagonal entries are zeroIdentity matrixdiagonal entries are 1AI = ATransposerows become columnsA shape: (m, n)A.T shape: (n, m)Symmetric matrixA = A.TTracesum of main diagonal entriesRanknumber of independent directionsSingular matrixno ordinary inverseInverseA @ A_inverse = I
```

Useful NumPy operations:

```
A.shapeA.Tnp.diag(A)np.trace(A)np.eye(n)np.linalg.det(A)np.linalg.matrix_rank(A)np.linalg.inv(A)np.linalg.solve(A, b)np.linalg.cond(A)np.allclose(A, B)
```

---

# 34. Practice exercises

## Exercise 1

For:

A=[147258369]A= \begin{bmatrix} 1 & 4 & 7\\ 2 & 5 & 8\\ 3 & 6 & 9 \end{bmatrix}A=​123​456​789​​

Find:

- Shape
- a23a_{23}a23​
- Second row
- Third column
- Main diagonal
- Trace
- Transpose
- Rank
- Determinant

---

## Exercise 2

Create these using NumPy:

- A 4×44\times44×4 zero matrix
- A 3×33\times33×3 identity matrix
- A diagonal matrix containing `[2, 4, 8]`
- A 2×52\times52×5 ones matrix
- An upper-triangular matrix
- A symmetric matrix

---

## Exercise 3

Write functions:

```
is_square(A)is_symmetric(A)is_diagonal(A)is_singular(A)has_full_rank(A)
```

Each function should validate that the input is two-dimensional.

---

# 35. Debugging assignment

The following code is broken or unsafe:

```
import numpy as npA = np.array([    [1, 2, 3],    [2, 4, 6]])print("Inverse:")print(np.linalg.inv(A))print("Symmetric:")print(A == A.T)x = np.array([1, 2, 3])print("Column vector:", x.T.shape)
```

Identify every issue and create a corrected version that:

- Handles rectangular matrices
- Checks whether an ordinary inverse exists
- Checks symmetry safely
- Creates an explicit column vector
- Reports rank and condition information

---

# 36. Real-world challenge

You are building a regression API.

The model expects:

```
Feature matrix shape: (batch_size, 5)
```

The API receives:

```
X = np.array([    [5.0, 80.0, 72.0],    [6.0, 85.0, 75.0],    [7.0, 90.0, 82.0],    [8.0, 92.0, 88.0],    [4.0, 70.0, 65.0]])
```

Its shape is:

```
(5, 3)
```

A developer assumes this means five features because the first shape value is five.

Your task:

1. Explain the mistake.
2. Determine how many observations and features are actually present.
3. Create a validation function.
4. Produce a descriptive error message.
5. Decide whether transposing the matrix is a valid solution or merely hides a data-contract problem.

---

# 37. Revision questions

1. Why are covariance matrices square?
2. Why are covariance matrices symmetric?
3. What information does matrix rank provide?
4. How are determinant and invertibility related?
5. Why can a matrix be invertible but numerically dangerous?
6. Why should `np.allclose()` be used for calculated matrices?
7. How does an identity matrix behave under multiplication?
8. What is the difference between an inverse and a pseudoinverse?
9. Why are sparse matrices useful in NLP?
10. How can redundant features affect regression?

---

# 38. Revision summary

- A matrix has rows, columns, entries and a defined shape.
- Rows and columns must have clear semantic meanings.
- Square matrices appear frequently in covariance, optimisation and transformations.
- A diagonal matrix contains zeros outside its main diagonal.
- The identity matrix leaves compatible objects unchanged.
- Transpose swaps matrix rows and columns.
- A symmetric matrix satisfies A=ATA=A^TA=AT.
- Trace is the sum of main-diagonal elements.
- Rank measures independent information or directions.
- A singular matrix has no ordinary inverse.
- A tiny determinant or large condition number may indicate numerical instability.
- Solving Ax=bA\mathbf{x}=\mathbf{b}Ax=b is generally safer with `np.linalg.solve()` than by explicitly calculating A−1A^{-1}A−1.
- Production systems must validate shape, rank, datatype, finite values and feature semantics.