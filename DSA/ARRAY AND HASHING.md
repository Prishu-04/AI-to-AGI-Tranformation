
### 📘 SUBTOPIC 1: Array Basics & Memory Layout
***
#### DEFINITION
**Simple:** An array is a collection of elements stored **side-by-side in memory**, all of the **same type**, accessible via an index.

**Formal:** An array is a contiguous block of memory of size `n × sizeof(type)`, where the `i-th` element is located at address:

```
base_address + (i × sizeof(element))
```
***
#### INTUITION — Real Life Analogy
🏨 **Think of a hotel corridor.**
- The hotel is your RAM
- Each room is a memory cell
- Room numbers are indices (0, 1, 2, ...)
- All rooms are **identical in size** (same data type)
- You can jump to **any room instantly** if you know the number → **O(1) access**
No searching required. You don't walk room by room — you teleport directly.
***
#### MEMORY LAYOUT (The Most Important Mental Model)
```
int arr[] = {10, 20, 30, 40, 50}

Index:    [  0  ] [  1  ] [  2  ] [  3  ] [  4  ]
Value:    [  10 ] [  20 ] [  30 ] [  40 ] [  50 ]
Address:  [1000 ] [1004 ] [1008 ] [1012 ] [1016 ]
           ↑
        base address
        (each int = 4 bytes)
```

**Formula:** `address of arr[i] = 1000 + i × 4`
This is why array access is **O(1)** — it's pure arithmetic, no traversal.
***
#### VISUAL UNDERSTANDING 🎥
**VisuAlgo (Interactive):** 🔗 [https://visualgo.net/en/array](https://visualgo.net/en/array) → Watch insert, delete, search animations step by step

**How to interpret:**
- Watch how the **pointer moves** when you index
- Notice insertion in the **middle** requires shifting — that's why it's O(n)
- Notice deletion leaves a **gap** unless shifted
***
#### WHEN TO USE ARRAYS

| Situation                               | Use Array?            |
| --------------------------------------- | --------------------- |
| Fixed-size data, fast access by index   | ✅ Yes                 |
| Frequent insertions/deletions at middle | ❌ No (use LinkedList) |
| Need to iterate over all elements       | ✅ Yes                 |
| Need key-value lookup                   | ❌ No (use HashMap)    |
| Cache-friendly sequential processing    | ✅ Yes                 |
***
#### EDGE CASES ⚠️
```
1. Empty array → always check if n == 0 before processing
2. Single element → many algorithms break on n == 1
3. All same elements → duplicates handling
4. Integer overflow → sum of large arrays (use long/long long)
5. Negative indices → undefined behavior in C++
6. Off-by-one → arr[n] is OUT OF BOUNDS (valid: 0 to n-1)
```
***
#### IMPLEMENTATION
##### C++
```C++
#include <iostream> 
#include <vector> 
using namespace std; 
int main() { 
	// Static array 
	int arr[5] = {10, 20, 30, 40, 50}; 
	// fixed size, stack memory 
	// Dynamic array (preferred in DSA) 
	vector<int> v = {10, 20, 30, 40, 50}; 
	
	// Access → O(1) 
	cout << v[2] << endl;
	// 30 — direct index access 
	
	// Traversal → O(n) 
	for (int i = 0; i < v.size(); i++) { 
		cout << v[i] << " "; 
	} 
	
	// Insert at end → O(1) amortized 
	v.push_back(60); 
	
	// Insert at middle → O(n) due to shifting
	v.insert(v.begin() + 2, 99); 
	// inserts 99 at index 2 
	
	// Delete from end → O(1) 
	v.pop_back(); 
	
	// Delete from middle → O(n) 
	v.erase(v.begin() + 2); 
	// removes element at index 2 
	
	// Size 
	cout << v.size() << endl; 
	return 0; }
```
##### Java
```Java
import java.util.ArrayList;
import java.util.Arrays;

public class ArrayBasics {
    public static void main(String[] args) {

        // Static array
        int[] arr = {10, 20, 30, 40, 50};  // fixed size

        // Dynamic array (preferred in DSA)
        ArrayList<Integer> list = new ArrayList<>(
            Arrays.asList(10, 20, 30, 40, 50)
        );

        // Access → O(1)
        System.out.println(list.get(2));       // 30

        // Traversal → O(n)
        for (int i = 0; i < list.size(); i++) {
            System.out.print(list.get(i) + " ");
        }

        // Insert at end → O(1) amortized
        list.add(60);

        // Insert at middle → O(n)
        list.add(2, 99);                       // inserts 99 at index 2

        // Delete from end → O(1)
        list.remove(list.size() - 1);

        // Delete from middle → O(n)
        list.remove(2);                        // removes index 2

        // Size
        System.out.println(list.size());
    }
}
```
***
#### PROBLEM SOLVING APPROACH
#### Problem: Find the maximum element in an array
**🔴 Brute Force (Sorting):**
```
Sort the array → last element is max
Time: O(n log n) | Space: O(1)
❌ Overkill — destroys original order
```

**🟡 Better (Two-pass thinking):
```
First pass to find max, second to find index
Time: O(n) | Still two passes — unnecessary
```

**🟢 Optimal (Single Pass):
```C++
int findMax(vector<int>& arr) {
    int maxVal = arr[0];           // assume first is max
    for (int i = 1; i < arr.size(); i++) {
        if (arr[i] > maxVal)       // update if larger found
            maxVal = arr[i];
    }
    return maxVal;
}
// Time: O(n) | Space: O(1) ✅
```
**Thought process:**

> "I need to look at every element at least once → O(n) is the floor. Can I do it in one pass? Yes — track a running maximum."

***
#### DRY RUN
```
arr = [3, 7, 1, 9, 4]

i=0: maxVal = 3  (initialized)
i=1: arr[1]=7  > 3  → maxVal = 7
i=2: arr[2]=1  < 7  → no change
i=3: arr[3]=9  > 7  → maxVal = 9
i=4: arr[4]=4  < 9  → no change

✅ Answer: 9
```
***
#### PATTERN RECOGNITION
Signals that scream "array pattern":
```
- "contiguous subarray"    → Sliding window or Kadane's
- "sorted array"           → Two pointers or Binary search
- "find pair/triplet"      → Two pointers or Hashing
- "range queries"          → Prefix sums
- "in-place modification"  → Two pointers
- "move zeros / partition" → Two pointer swap
```
***
#### QUESTIONS

![[Pasted image 20260504134740.png]]
***
#### COMMON MISTAKES ❌
```
1. ❌ Accessing arr[n] → always go up to arr[n-1]
2. ❌ Not handling empty array → check n==0 first
3. ❌ Using int for sum of large arrays → use long long in C++, long in Java
4. ❌ Modifying array while iterating → causes skipped elements
5. ❌ Confusing size() with last index → last index = size()-1
6. ❌ Shallow copy of arrays → arr2 = arr1 in Java copies reference, not values
```
***
#### COMPLEXITY SUMMARY
![[Pasted image 20260504135329.png]]

