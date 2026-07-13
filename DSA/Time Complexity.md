# Define
**Time complexity** describes how an algorithm’s running time grows as the size of its input increases.
It does **not** measure the exact execution time in seconds. Instead, it measures the **number of operations** performed for an input of size `n`.
![[Pasted image 20260713104641.png]]
![[Pasted image 20260713134115.png]]

---
## 1. Constant Time - `O(1)`
The number of operations does not depend on input size.
```Java
int value = arr[0];
```
Whether the array has 10 or 10,000 elements, accessing `arr[0]` takes one operation.

---
## 2. Linear Time - `O(n)`
The number of operations grows directly with input size.
```Java
for (int i = 0; i < n; i++) {
    System.out.println(arr[i]);
}
```
For `n = 10`, approximately 10 iterations occur.  
For `n = 100`, approximately 100 iterations occur.

---
## 3. Quadratic Time — `O(n²)`
Usually occurs with two nested loops.
```Java
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        System.out.println(i + " " + j);
    }
}
```
The outer loop runs `n` times, and for every outer iteration, the inner loop runs `n` times:
![[Pasted image 20260713104941.png|103]]
Therefore, the complexity is `O(n²)`.

---
## 4. Logarithmic Time - `O(logn)`
The input size is repeatedly divided, usually by 2.
```Java
while (n > 1) {
    n = n / 2;
}
```
For example:
```
16 → 8 → 4 → 2 → 1
```
Only four operations are needed for `n = 16`, so the complexity is `O(log n)`.

---
## Rules for Calculating Time Complexity
### Ignore constants
```Java
for (int i = 0; i < 2 * n; i++) {
    // operation
}
```
The exact complexity is `O(2n)`, but constants are ignored:
![[Pasted image 20260713105126.png|123]]
### Keep the fastest-growing term
```
O(n² + n + 10)
```
For large values of `n`, `n²` dominates the other terms:
![[Pasted image 20260713105144.png|171]]
### Consecutive loops are added
```Java
for (int i = 0; i < n; i++) {
    // O(n)
}
for (int i = 0; i < n; i++) {
    // O(n)
}
```
Total:
![[Pasted image 20260713105209.png|275]]
### Nested loops are multiplied
```Java
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        // operation
    }
}
```
Total:
![[Pasted image 20260713105242.png|216]]
In simple terms, **time complexity tells us how efficient an algorithm will remain when the input becomes very large.**

---
# Important Time Complexity Patterns
The biggest mistake is assuming:
- One loop always means `O(n)`
- Two nested loops always mean `O(n²)`
- Recursion always means exponential
The actual complexity depends on **how the loop variable changes**, **whether pointers reset**, and **how many recursive calls are created**.

---
## 1. Constant Time - `O(1)`
The number of operations does not grow with `n`.
### Example 1: Direct array access
```Java
int value = arr[n / 2];
```
Even though `n` is used, only one array element is accessed.
### Example 2: Fixed number of iterations
```Java
for (int i = 0; i < 100; i++) {
    System.out.println(i);
}
```
The loop always runs 100 times, regardless of `n`.
![[Pasted image 20260713131034.png|141]]
**Pattern:** A constant loop limit gives `O(1)`.
## Example 3: Loop starting from `n`
```Java
for (int i = n; i < n + 50; i++) {
    System.out.println(i);
}
```
This may look dependent on `n`, but it always runs exactly 50 times.
## Example 4: Mathematical formula
```Java
int sum = n * (n + 1) / 2;
```
It calculates the sum of the first `n` numbers without a loop.
## Example 5: Conditional statement
```Java
if (n % 2 == 0) {
    System.out.println("Even");
} else {
    System.out.println("Odd");
}
```
Only one condition and one output operation are performed.

---
# 2. Logarithmic Time - `O(logn)`
The input is repeatedly multiplied or divided by a constant.
## Example 1: Multiplication by 2
```Java
for (int i = 1; i < n; i *= 2) {
    System.out.println(i);
}
```
Values of `i`:
```
1, 2, 4, 8, 16, 32...
```
![[Pasted image 20260713131340.png]]
## Example 2: Division by 2
```Java
for (int i = n; i > 0; i /= 2) {
    System.out.println(i);
}
```
For `n = 16`:
```
16 → 8 → 4 → 2 → 1
```
Complexity:
![[Pasted image 20260713131444.png|81]]

---
## Example 3: Multiplication by 3
```Java
for(int i=0;i<n;i*=3){
	System.out.println(i);
}
```
![[Pasted image 20260713131558.png]]

---
## Example 4: Binary Search
```Java
int low = 0;
int high = arr.length - 1;

while (low <= high) {
    int mid = low + (high - low) / 2;

    if (arr[mid] == target) {
        break;
    } else if (arr[mid] < target) {
        low = mid + 1;
    } else {
        high = mid - 1;
    }
}
```
---
## Example 5: Recursive halving
```Java
static void solve(int n) {
    if (n <= 1) {
        return;
    }

    solve(n / 2);
}
```
![[Pasted image 20260713131754.png]]

---
# 3. Linear Time - `O(n)`
The number of operations grows proportionally with `n`.
## Example 1: Incrementing by 2
```Java
for (int i = 0; i < n; i += 2) {
    System.out.println(i);
}
```
The loop runs approximately `n/2` times.
![[Pasted image 20260713131914.png|144]]
**Important:** Increasing by a constant still gives `O(n)`

---
## Example 2: Two consecutive loops
```Java
for (int i = 0; i < n; i++) {
    System.out.println(i);
}
for (int i = 0; i < n; i++) {
    System.out.println(i);
}
```
![[Pasted image 20260713131950.png]]

---
## Example 3: Nested loop with constant inner loop
```Java
for (int i = 0; i < n; i++) {
    for (int j = 0; j < 10; j++) {
        System.out.println(i + " " + j);
    }
}
```
![[Pasted image 20260713132015.png]]

---
## Example 4: Two-pointer technique
```Java
int left = 0;
int right = n - 1;

while (left < right) {
    if (arr[left] + arr[right] == target) {
        break;
    } else if (arr[left] + arr[right] < target) {
        left++;
    } else {
        right--;
    }
}
```
Both pointers together move at most `n` times.
![[Pasted image 20260713132107.png|59]]
It is not `O(n²)` because neither pointer resets.

---
## Example 5: Nested loops that are still `O(n)`
```Java
for (int i = 1; i < n; i *= 2) {
    for (int j = 0; j < i; j++) {
        System.out.println(j);
    }
}
```
![[Pasted image 20260713132136.png]]

---
# 4. Linearithmic Time - `O(nlogn)`
Usually appears when:
- A linear operation is performed for every logarithmic level.
- A logarithmic operation is performed `n` times.
## Example 1: Linear loop with logarithmic inner loop
```Java
for (int i = 0; i < n; i++) {
    for (int j = 1; j < n; j *= 2) {
        System.out.println(i + " " + j);
    }
}
```
![[Pasted image 20260713132235.png]]

--- 
## Example 2: Inner loop depends on `ì`
```java
for (int i = 1; i <= n; i++) {
    for (int j = 1; j <= i; j *= 2) {
        System.out.println(i + " " + j);
    }
}
```
![[Pasted image 20260713132411.png]]

---
## Example 3: Merge sort
```Java
static void mergeSort(int[] arr, int left, int right) {
    if (left >= right) {
        return;
    }
    int mid = left + (right - left) / 2;
    mergeSort(arr, left, mid);
    mergeSort(arr, mid + 1, right);
    merge(arr, left, mid, right);
}
```
There are `log n` recursive levels.
At every level, merging takes `O(n)`.
![[Pasted image 20260713132521.png|241]]

---
## Example 4: Comparison-based sorting
```Java
Arrays.sort(arr);
```
For primitive arrays, Java typically uses optimized sorting algorithms whose expected or worst-case behavior depends on the implementation and data type.
Common comparison sorting complexities include:
![[Pasted image 20260713132609.png|101]]
Examples include:
- Merge sort
- Heap sort
- Average-case quicksort
Always include the complexity of library methods in your analysis.

---
## Example 5: Inserting `n` elements into a heap
```Java
PriorityQueue<Integer> heap = new PriorityQueue<>();
for (int value : arr) {
    heap.offer(value);
}
```
![[Pasted image 20260713132639.png]]

--- 
# 5. Quadratic Time - `O(n2)`
Usually appears when every element is compared or combined with many other elements.
## Example 1: Two complete nested loops
```Java
for (int i = 0; i < n; i++) {
    for (int j = 0; j < n; j++) {
        System.out.println(i + " " + j);
    }
}
```
![[Pasted image 20260713132930.png]]
## Example 2: Triangular nested Loop
```Java
for (int i = 0; i < n; i++) {
    for (int j = 0; j <= i; j++) {
        System.out.println(i + " " + j);
    }
}
```
The iterations are:
```
1 + 2 + 3 + ... + n
```
![[Pasted image 20260713133032.png]]
## Example 3: Inner loop starts from `i`
```Java
for (int i = 0; i < n; i++) {
    for (int j = i; j < n; j++) {
        System.out.println(i + " " + j);
    }
}
```
Iterations:
```
n + (n-1) + (n-2) + ... + 1
```
![[Pasted image 20260713133222.png]]

---
## Example 4: Pointer resets during every iteration
```Java
for (int i = 0; i < n; i++) {
    int j = 0;
    while (j < n) {
        j++;
    }
}
```
![[Pasted image 20260713133313.png]]
## Example 5: String concatenation inside a loop
```Java
String result = "";
for (int i = 0; i < n; i++) {
    result = result + arr[i];
}
```
Java `String` objects are immutable.
Every concatenation may create a new string and copy the previous content:
```
1 + 2 + 3 + ... + n
```
![[Pasted image 20260713133359.png]]
Use `StringBuilder` instead:
```Java
StringBuilder result = new StringBuilder();
for (int i = 0; i < n; i++) {
    result.append(arr[i]);
}
```
![[Pasted image 20260713133442.png]]

---
# 6. Exponential Time — `O(2ⁿ)`
Usually appears when every recursive call creates two possibilities.
## Example 1: Two recursive calls
```Java
static void solve(int n) {
    if (n == 0) {
        return;
    }
    solve(n - 1);
    solve(n - 1);
}
```
Each call creates two more calls.
Number of calls:
```
1 + 2 + 4 + 8 + ... + 2ⁿ
```
## Example 2: Include or exclude an element
```Java
static void generateSubsets(int[] arr, int index) {
    if (index == arr.length) {
        return;
    }
    generateSubsets(arr, index + 1); // Exclude
    generateSubsets(arr, index + 1); // Include
}
```
![[Pasted image 20260713133730.png]]
## Example 3: Generating binary strings
```Java
static void generate(String current, int n) {
    if (current.length() == n) {
        System.out.println(current);
        return;
    }
    generate(current + "0", n);
    generate(current + "1", n);
}
```
![[Pasted image 20260713133809.png]]
## Example 4: Naive Fibonacci
```Java
static int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n - 1) + fibonacci(n - 2);
}
```
The recursive calls repeatedly recompute the same values.
![[Pasted image 20260713133910.png]]
## Example 5: Tower of Hanoi
```java
static void hanoi(int n, char source, char helper, char destination) {
    if (n == 0) {
        return;
    }
    hanoi(n - 1, source, destination, helper);
    System.out.println(source + " -> " + destination);
    hanoi(n - 1, helper, source, destination);
}
```
![[Pasted image 20260713134007.png]]

--- 
# 7. Factorial Time — `O(n!)`
Usually appears when every possible ordering or permutation is generated.
## Example 1: Generating permutations
```Java
static void permute(int[] arr, int index) {
    if (index == arr.length) {
        System.out.println(Arrays.toString(arr));
        return;
    }
    for (int i = index; i < arr.length; i++) {
        swap(arr, index, i);
        permute(arr, index + 1);
        swap(arr, index, i);
    }
}
```
Choices:
```
n × (n-1) × (n-2) × ... × 1
```
![[Pasted image 20260713134210.png]]
## Example 2: Travelling Salesman brute force
Suppose every possible city order is checked.
```Java
generateAllRoutes(cities);
```
![[Pasted image 20260713134248.png]]
## Example 3: N-Queens backtracking
For every row, try placing a queen in available columns.
```Java
static void solve(int row, int n) {
    if (row == n) {
        return;
    }
    for (int col = 0; col < n; col++) {
        if (isSafe(row, col)) {
            placeQueen(row, col);
            solve(row + 1, n);
            removeQueen(row, col);
        }
    }
}
```
![[Pasted image 20260713134330.png]]
## Example 4: Assigning jobs to people
Suppose there are:
- `n` workers
- `n` jobs
Every worker must receive exactly one job.
![[Pasted image 20260713134357.png]]
## Example 5: Factorial recursive branching
```Java
static void solve(int n) {
    if (n == 0) {
        return;
    }
    for (int i = 0; i < n; i++) {
        solve(n - 1);
    }
}
```
![[Pasted image 20260713134451.png]]

---
# Additional Important Exception Patterns
## 1. Square-root complexity — `O(√n)`
```Java
for (int i = 1; i * i <= n; i++) {
    System.out.println(i);
}
```
![[Pasted image 20260713134549.png]]
```Java
static boolean isPrime(int n) {
    for (int i = 2; i * i <= n; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return n >= 2;
}
```
---
## 2. Log-log complexity — `O(log log n)`
```java
for (int i = 2; i < n; i *= i) {
    System.out.println(i);
}
```
Values grow extremely quickly:
```
2 → 4 → 16 → 256 → 65536
```
![[Pasted image 20260713134702.png]]

---
## 3. Multiple independent inputs — `O(nm)`
```java
for (int i = 0; i < n; i++) {
    for (int j = 0; j < m; j++) {
        System.out.println(i + " " + j);
    }
}
```
Complexity :
```
O(nm)
```
---
## 4. Amortized `O(1)`
```Java
ArrayList<Integer> list = new ArrayList<>();
list.add(value);
```
![[Pasted image 20260713134824.png]]

---
![[Pasted image 20260713134845.png]]

---
# Most Important Rules to Remember
### Rule 1: `i++`, `i += 2`, `i += 100`
These are generally:
```
O(n)
```
because the variable changes by a constant amount.
### Rule 2: `i *= 2`, `i /= 2`
These are generally:
```
O(log⁡n)
```
because the value changes multiplicatively.
### Rule 3: `i *= i`
This can produce:
```
O(log⁡log⁡n)
```
### Rule 4: `i * i <= n`
This generally produces:
![[Pasted image 20260713135047.png|68]]
### Rule 5: Nested loops
Do not blindly multiply. First check:
- Does the inner loop reset?
- Does it depend on the outer variable?
- Does it run a constant number of times?
- Is the total a geometric series?
### Rule 6: Recursion
Write the recurrence:
```
One call with n/2        → O(log n)
Two calls with n/2       → often O(n)
Two calls with n-1       → O(2ⁿ)
n calls with n-1         → O(n!)
```
### Rule 7: Include hidden operations
Check the complexity of:
- Sorting
- String concatenation
- Array copying
- HashMap operations
- List insertion/deletion
- Recursive output printing
- Library functions
The most important lesson is: **count the total number of operations, not merely the number of visible loops.**

---
