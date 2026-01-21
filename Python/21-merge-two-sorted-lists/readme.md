# Merge Two Sorted Lists (LeetCode Problem 21)
## Problem Statement
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return *the head of the merged linked list.*

 

### Example 1:
![alt text](image.png)
```
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
```
### Example 2:
```
Input: list1 = [], list2 = []
Output: []
```
### Example 3:
```
Input: list1 = [], list2 = [0]
Output: [0]
 ```

## Constraints:

- The number of nodes in both lists is in the range `[0, 50]`.
- `-100 <= Node.val <= 100`
- Both `list1` and `list2` are sorted in non-decreasing order.

## Algorithm
**Input:** Two sorted lists (arrays), referred to here as `List A` and `List B`.

**Output:** A single sorted list containing all elements from both inputs.


1. Initialization:
    - Create two integer pointers (indices), `i` and `j`, and set both to `0`.
    - Create an empty list (or array) called `merged_list` to store the result.
2. Comparison Loop:
    - While pointer `i` is less than the length of `List A` AND pointer `j` is less than the length of `List B`:
        - Compare the element at `List A[i]` with the element at `List B[j]`.
        - If `List A[i]` is smaller (or equal):
            - Append `List A[i]` to `merged_list`.
            - Increment pointer` i `by `1`.
        - Else (if `List B[j]` is smaller):
            - Append `List B[j]` to `merged_list`.
            - Increment pointer `j` by `1`.
3. Handle Remaining Elements:
    - Once the loop terminates, one list will be empty, but the other may still have elements left.
    - Check if there are remaining elements in `List A `(starting from index `i`). If yes, append all of them to `merged_list`.
    - Check if there are remaining elements in `List B` (starting from index `j`). If yes, append all of them to `merged_list`.
4. Termination:
    - Return the `merged_list`.