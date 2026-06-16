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
It could represent:
- Three students
- Three features per student
- Rows as observations
- Columns as features
Now consider a neural-network weight matrix:
![[Pasted image 20260616120236.png|201]]
This matrix does not represent a dataset. It represents a transformation from three input features to two output units.
The matrix’s meaning depends on:
- Its shape
- The meaning assigned to rows and columns
- Its internal structure
- The operation in which it is used

---
## 3. Industry applications

### Neural networks
Every dense neural-network layer contains a weight matrix:
![[Pasted image 20260616120321.png|153]]
The shape of WWW determines:
- How many inputs the layer accepts
- How many outputs it generates
- How many trainable parameters it contains
### Recommendation systems
A user-item interaction matrix may look like:
![[Pasted image 20260616120343.png|140]]
Rows may represent users, while columns represent products, songs or movies.
### Computer vision
Matrices represent:
- Grayscale images
- Convolution filters
- Geometric transformations
- Feature maps
- Attention maps
### Natural language processing
Matrices are used for:
- Token embeddings
- Attention scores
- Query, key and value transformations
- Vocabulary projections
- Batches of hidden representations
### Financial and scientific systems
Matrices can represent:
- Asset covariance
- Customer transactions
- Sensor readings
- Physical transformations
- Linear constraints
- Risk relationships
Major AI systems built by organisations such as Google, Microsoft, Meta, NVIDIA, Amazon, Netflix and OpenAI depend heavily on matrix and tensor operations.

---
## 4. Interview relevance
Common interview questions include:
```
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
```
Production-oriented interviews may ask:
```
- How would you validate matrix inputs?
- Why can a matrix operation consume excessive memory?
- How do you detect a rank-deficient feature matrix?
- Why should you avoid explicitly computing matrix inverses?
- How do sparse matrices reduce memory usage?
```
---
## 5. Basic matrix notation
A general matrix with mmm rows and nnn columns is written as:
![[Pasted image 20260616120510.png]]
This means:
- A contains real numbers.
- A has m rows.
- A has n columns.

---
### Example
![[Pasted image 20260616120542.png|149]]
It has:
- 2 rows
- 3 columns
- Shape 2×32\times32×3
- 6 total entries
Therefore:
![[Pasted image 20260616120606.png|89]]

---
## 6. Matrix entries
The notation `aij`​ means:
- i: row number
- j: column number
For:
![[Pasted image 20260616120649.png|396]]
### Important difference from Python
Mathematical indexing usually starts from 1.
Python indexing starts from 0.
Therefore:
a23
corresponds to:
```
A[1, 2]
```
---
### NumPy implementation
![[Pasted image 20260616120854.png]]

---
## 7. Rows and columns
![[Pasted image 20260616120914.png]]
### NumPy
![[Pasted image 20260616121007.png]]
Notice that both results have shape `(3,)` or `(2,)`, not explicit row or column shapes.
To preserve two-dimensional structure:
![[Pasted image 20260616121046.png]]
This difference becomes important during matrix multiplication.

---
## 8. Types of matrices
### 8.1 Rectangular matrix
A rectangular matrix has a different number of rows and columns.
![[Pasted image 20260616121105.png|137]]
Shape:
![[Pasted image 20260616121119.png|47]]
Most ML datasets are rectangular because the number of observations is usually different from the number of features.
```
A = np.array([    
	[1, 2, 3],    
	[4, 5, 6]])
print(A.shape)
```
---
### 8.2 Square matrix
A square matrix has the same number of rows and columns.
![[Pasted image 20260616121232.png]]
Square matrices appear in:
- Covariance matrices
- Correlation matrices
- Transformation matrices
- Hessian matrices
- Attention-score matrices
- Systems of equations
```
A = np.array([    
	[1, 2],    
	[3, 4]])
is_square = A.shape[0] == A.shape[1]
print("Square matrix:", is_square)
```
![[Pasted image 20260616121305.png]]

---
### 8.3 Row matrix
A row matrix contains exactly one row.
![[Pasted image 20260616121326.png]]
![[Pasted image 20260616121401.png]]

---
### 8.4 Column matrix
A column matrix contains exactly one column.
![[Pasted image 20260616121446.png]]
![[Pasted image 20260616121520.png]]

---
### 8.5 Zero matrix
![[Pasted image 20260616121545.png]]
![[Pasted image 20260616121621.png]]
### ML applications
Zero matrices may be used for:
- Initial placeholders
- Masks
- Gradient buffers
- Padding
- Empty accumulators
However, initializing all neural-network weights to zero can prevent neurons from learning different features because of symmetry.

---
### 8.6 Ones matrix
A ones matrix contains only ones.
![[Pasted image 20260616121647.png|127]]
![[Pasted image 20260616121721.png]]
Applications include:
- Masks
- Baseline arrays
- Initialisation experiments
- Broadcasting demonstrations

---
## 9. Diagonal matrices
A diagonal matrix is a square matrix where all off-diagonal entries are zero.
![[Pasted image 20260616121742.png]]
### Why diagonal matrices are useful
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
### NumPy
![[Pasted image 20260616121833.png]]

---
### Checking whether a matrix is diagonal
![[Pasted image 20260616121920.png]]

---
## 10. Identity matrix
An identity matrix is a diagonal matrix containing ones along the main diagonal.
![[Pasted image 20260616121942.png]]
provided the shapes are compatible.
### Intuition
The identity matrix performs no transformation.
If a vector enters an identity transformation, it leaves unchanged.
![[Pasted image 20260616122014.png]]
### ML applications
Identity matrices appear in:
- Regularisation
- Numerical stabilisation
- Residual connections
- Covariance calculations
- Initial transformations
- Matrix inverse formulas
For example, ridge regression uses a term related to:
![[Pasted image 20260616122039.png|106]]
The identity matrix adds regularisation independently to model parameters.

---
## 11. Scalar matrix
A scalar matrix is an identity matrix multiplied by a scalar.
![[Pasted image 20260616122100.png|203]]
![[Pasted image 20260616122134.png]]
It scales every coordinate equally.

---
## 12. Triangular matrices
### Upper triangular matrix
All entries below the main diagonal are zero.
![[Pasted image 20260616122203.png|157]]
![[Pasted image 20260616122240.png]]
### Lower triangular matrix
All entries above the main diagonal are zero.
![[Pasted image 20260616122311.png|154]]
![[Pasted image 20260616122339.png]]
### Why triangular matrices matter
They appear in:
- Gaussian elimination
- Solving linear systems
- LU decomposition
- Cholesky decomposition
- Numerical optimisation
Triangular systems are usually easier and faster to solve than general systems.

---
## 13. Matrix transpose
The transpose swaps rows and columns.
![[Pasted image 20260616122417.png]]
### NumPy
![[Pasted image 20260616122454.png]]

---
### Critical NumPy trap
```
x = np.array([1, 2, 3])
print(x.shape)
print(x.T.shape)
```
Output:
```
(3,)(3,)
```
The transpose does not change a one-dimensional array.
To create a column vector:
```
x_column = x.reshape(-1, 1)
print(x_column)
print(x_column.shape)
```
Output:
```
[[1] [2] [3]](3, 1)
```
To create a row vector:
```
x_row = x.reshape(1, -1)
print(x_row.shape)
```
Output:
```
(1, 3)
```

---
## 14. Transpose properties
For compatible matrices:
![[Pasted image 20260616122710.png]]
Notice that the order reverses.
This will become important in matrix multiplication and gradient derivations.

---
## 15. Symmetric matrix
A square matrix is symmetric when:
![[Pasted image 20260616122749.png]]
The values mirror across the main diagonal.
### NumPy check
![[Pasted image 20260616122820.png]]
Use `np.allclose()` rather than exact equality when working with floating-point calculations.
#### ML importance
These matrices are often symmetric:
- Covariance matrices
- Correlation matrices
- Hessian matrices
- Gram matrices
- Kernel matrices
Symmetric matrices have useful mathematical properties that will matter when studying eigenvalues, eigenvectors and PCA.

---
## 16. Main diagonal and trace
![[Pasted image 20260616122854.png]]
### NumPy
![[Pasted image 20260616122940.png]]
### ML significance
For a covariance matrix, the trace equals the total variance across its diagonal features.
Trace also appears in:
- Matrix calculus
- Optimisation objectives
- Statistical estimation
- Regularisation
- Dimensionality reduction
---
## 17. Determinant intuition
The determinant is a scalar associated with a square matrix.
![[Pasted image 20260616123430.png]]
### Geometric intuition
A matrix transforms space.
The absolute determinant tells us how much the transformation scales area or volume.
![[Pasted image 20260616123456.png]]
the matrix is singular and has no inverse.
### NumPy
![[Pasted image 20260616123637.png]]
Because of floating-point calculations, you may see:
```
4.999999999999999
```
instead of exactly `5`.

---
## 18. Matrix rank intuition
Rank tells us how many independent directions or independent pieces of information a matrix contains.
Consider:
![[Pasted image 20260616123701.png|147]]
The second row is twice the first row.
Therefore, the second row does not provide new independent information.
The matrix has rank 1, not rank 2.
![[Pasted image 20260616123743.png]]

---
### Full rank
![[Pasted image 20260616123802.png|517]]
Example:
![[Pasted image 20260616123833.png]]

---
### Why rank matters in ML
Suppose two dataset features are identical:
```
monthly_salary
annual_salary / 12
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
## 19. Inverse matrix intuition
![[Pasted image 20260616123947.png]]
### Example
![[Pasted image 20260616124020.png]]
### NumPy
![[Pasted image 20260616124050.png]]```

---
### When does an inverse exist?
A matrix must generally be:
1. Square
2. Full rank
3. Non-singular
4. Have a nonzero determinant
For a square matrix:
```
det⁡(A)≠0
```
is required for an inverse.

---
### Production engineering warning
Do not usually solve a linear system by explicitly calculating:
```Python
x = np.linalg.inv(A) @ b
```
Prefer:
```Python
x = np.linalg.solve(A, b)
```
Why?
- More numerically stable
- Usually faster
- Avoids unnecessary inverse construction
- Uses specialised numerical methods

---
## 20. Singular matrix
A singular matrix has no inverse.
![[Pasted image 20260616124239.png]]
![[Pasted image 20260616124430.png]]
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
## 21. Matrix as a linear transformation
A matrix can transform a vector.
![[Pasted image 20260616124458.png]]
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
## 22. Systems of linear equations
Consider:
![[Pasted image 20260616124532.png]]
### NumPy solution
![[Pasted image 20260616124604.png]]
Verification:
![[Pasted image 20260616124638.png]]
Both should be approximately equal.

---
## 23. Design matrix in machine learning
A feature matrix is often called a **design matrix**.
![[Pasted image 20260616124656.png]]
### NumPy
![[Pasted image 20260616124727.png]]

---
## 24. Coding laboratory: matrix inspector
```Python
from __future__ import annotations

  

import numpy as np

from numpy.typing import NDArray

  
  

def inspect_matrix(matrix: NDArray[np.float64]) -> dict[str, object]:

    if not isinstance(matrix, np.ndarray):

        raise TypeError("matrix must be a NumPy array.")

  

    if matrix.ndim != 2:

        raise ValueError(

            f"Expected a 2D matrix, received shape {matrix.shape}."

        )

  

    rows, columns = matrix.shape

    is_square = rows == columns

  

    report: dict[str, object] = {

        "shape": matrix.shape,

        "rows": rows,

        "columns": columns,

        "size": matrix.size,

        "dtype": str(matrix.dtype),

        "is_square": is_square,

        "rank": int(np.linalg.matrix_rank(matrix)),

        "contains_nan": bool(np.isnan(matrix).any()),

        "contains_infinity": bool(np.isinf(matrix).any())

    }

  

    if is_square:

        report["trace"] = float(np.trace(matrix))

        report["determinant"] = float(np.linalg.det(matrix))

        report["is_symmetric"] = bool(

            np.allclose(matrix, matrix.T)

        )

        report["is_diagonal"] = bool(

            np.allclose(matrix, np.diag(np.diag(matrix)))

        )

  

    return report

  
  

A = np.array([

    [2.0, 1.0],

    [1.0, 3.0]

])

  

report = inspect_matrix(A)

  

for key, value in report.items():

    print(f"{key}: {value}")
```
![[Pasted image 20260616124933.png]]

---
## 25. Safer structural checks
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
determinant = np.linalg.det(A)
is_nearly_singular = np.isclose(determinant, 0.0)
```
However, determinant alone is not always the most reliable numerical diagnostic. Condition numbers and singular values are often more informative.

---
## 26. Condition-number awareness
A matrix can technically be invertible but still be nearly singular.
Such a matrix is called **ill-conditioned**.
Small input changes may produce large output changes.
![[Pasted image 20260616125100.png]]
A large condition number suggests numerical instability.
### ML relevance
Poor conditioning can result from:
- Features with drastically different scales
- Strongly correlated features
- Duplicate information
- Bad numerical precision
- Poorly designed optimisation problems
Feature scaling can often improve conditioning and gradient-descent performance.

---
## 27. Sparse versus dense matrices
A dense matrix stores every entry, including zeros.
A sparse matrix stores mainly nonzero values and their locations.
Example:
![[Pasted image 20260616125134.png|173]]
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
![[Pasted image 20260616125325.png]]

---
## 28. Debugging laboratory
### Bug 1: Transposing a one-dimensional vector
Broken assumption:
```
x = np.array([1, 2, 3])
x_transpose = x.Tprint(x_transpose.shape)
```
Output:
```
(3,)
```
### Root cause
A one-dimensional array has no explicit row or column axis to swap.
### Correction
```
x_column = x.reshape(-1, 1)
x_row = x_column.Tprint(x_column.shape)print(x_row.shape)
```
---
### Bug 2: Inverting a rectangular matrix
Broken code:
```
A = np.array([    [1.0, 2.0, 3.0],    [4.0, 5.0, 6.0]])
np.linalg.inv(A)
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
### Bug 3: Singular matrix
```
A = np.array([    [1.0, 2.0],    [2.0, 4.0]])
np.linalg.inv(A)
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
### Bug 4: Exact floating-point equality
Broken code:
```
result = A @ np.linalg.inv(A)
print(result == np.eye(A.shape[0]))
```
Some values may unexpectedly be `False`.
### Root cause
Floating-point calculations contain small approximation errors.
### Correction
```
print(np.allclose(result, np.eye(A.shape[0])))
```
---
### Bug 5: Incorrect feature orientation
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
expected_features = 5
if X.shape[1] != expected_features:    
	raise ValueError(        
		f"Expected {expected_features} features, "
		f"received shape {X.shape}."
    )
```
---
## 29. Top 10 common errors
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
## 30. How senior engineers approach matrix problems
Before running an operation, they inspect:
```
print("Shape:", A.shape)
print("Dimensions:", A.ndim)
print("Datatype:", A.dtype)
print("Finite:", np.isfinite(A).all())
print("Rank:", np.linalg.matrix_rank(A))
```
For square matrices, they may also inspect:
```
print("Determinant:", np.linalg.det(A))
print("Condition number:", np.linalg.cond(A))
print("Symmetric:", np.allclose(A, A.T))
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
## 31. Knowledge checkpoint
Answer these without looking back.
### Question 1
What is the shape of this matrix?
![[Pasted image 20260616125658.png|108]]
### Question 2
What is the transpose shape of a 7×4 matrix?
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
x = np.array([1, 2, 3])
print(x.T.shape)
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
## 32. Interview questions
### Beginner
1. What is a matrix entry?
2. What does A∈Rm×nA\in\mathbb{R}^{m\times n}A∈Rm×n mean?
3. What is a square matrix?
4. What is a diagonal matrix?
5. What is an identity matrix?
6. What does matrix transpose do?
### Intermediate
7. What is a symmetric matrix?
8. What does the determinant represent geometrically?
9. What does rank tell us?
10. What is a singular matrix?
11. When does a square matrix have an inverse?
12. Why can duplicate features cause rank deficiency?
### Advanced interview traps
#### Trap 1
**Does every square matrix have an inverse?**
No. It must also be full rank or non-singular.
#### Trap 2
**If the determinant is very small but nonzero, is inversion safe?**
Not necessarily. The matrix may be ill-conditioned.
#### Trap 3
**Is `x.T` always a column vector?**
No. For a one-dimensional NumPy array, `.T` does not change its shape.
#### Trap 4
**Does a high-dimensional matrix always have high rank?**
No. Its rows or columns may contain redundant information.
#### Trap 5
**Should you compute an inverse to solve every linear system?**
No. Use a linear-system solver when possible.

---
## 33. Slot cheat sheet

```
Matrix shape
(rows, columns)

Square matrix
rows == columns

Diagonal matrix
off-diagonal entries are zero

Identity matrix
diagonal entries are 1
AI = A

Transpose
rows become columns
A shape: (m, n)
A.T shape: (n, m)

Symmetric matrix
A = A.T

Trace
sum of main diagonal entries

Rank
number of independent directions

Singular matrix
no ordinary inverse

Inverse
A @ A_inverse = Ishape: (m, n)A.T shape: (n, m)Symmetric matrixA = A.TTracesum of main diagonal entriesRanknumber of independent directionsSingular matrixno ordinary inverseInverseA @ A_inverse = I
```
Useful NumPy operations:
```Python
A.shape
A.T
np.diag(A)
np.trace(A)
np.eye(n)
np.linalg.det(A)
np.linalg.matrix_rank(A)
np.linalg.inv(A)
np.linalg.solve(A, b)
np.linalg.cond(A)
np.allclose(A, B)
```
---
## 34. Practice exercises
### Exercise 1
For:
![[Pasted image 20260616125913.png|139]]
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
### Exercise 2
Create these using NumPy:
- A 4×4 zero matrix
- A 3×3 identity matrix
- A diagonal matrix containing `[2, 4, 8]`
- A 2×5 ones matrix
- An upper-triangular matrix
- A symmetric matrix
---
### Exercise 3
Write functions:
```
is_square(A)
is_symmetric(A)
is_diagonal(A)
is_singular(A)
has_full_rank(A)
```
Each function should validate that the input is two-dimensional.

---
## 35. Debugging assignment
The following code is broken or unsafe:
```Python
import numpy as np

A = np.array([
    [1, 2, 3],
    [2, 4, 6]
])

print("Inverse:")
print(np.linalg.inv(A))

print("Symmetric:")
print(A == A.T)

x = np.array([1, 2, 3])
print("Column vector:", x.T.shape)
```
Identify every issue and create a corrected version that:
- Handles rectangular matrices
- Checks whether an ordinary inverse exists
- Checks symmetry safely
- Creates an explicit column vector
- Reports rank and condition information
---
## 36. Real-world challenge
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
## 37. Revision questions
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
## 38. Revision summary
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
---
