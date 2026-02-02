# Triangle Judgement (LeetCode Problem 610)
## Problem Statement
Table: `Triangle`
```
+-------------+------+
| Column Name | Type |
+-------------+------+
| x           | int  |
| y           | int  |
| z           | int  |
+-------------+------+
In SQL, (x, y, z) is the primary key column for this table.
Each row of this table contains the lengths of three line segments.
 ```

Report for every three line segments whether they can form a triangle.

Return the result table in any order.

The result format is in the following example.

 

### Example 1:
```
Input: 
Triangle table:
+----+----+----+
| x  | y  | z  |
+----+----+----+
| 13 | 15 | 30 |
| 10 | 20 | 15 |
+----+----+----+
Output: 
+----+----+----+----------+
| x  | y  | z  | triangle |
+----+----+----+----------+
| 13 | 15 | 30 | No       |
| 10 | 20 | 15 | Yes      |
+----+----+----+----------+
```
## Approach
To determine if three lengths can form a triangle, we use the Triangle Inequality Theorem. It’s a simple but strict rule:
```
The sum of the lengths of any two sides of a triangle must be greater than the length of the third side.
```
If even one pair fails this test, the lines cannot meet to form a closed shape—they would either lie flat (if the sum equals the third side) or never touch (if the sum is less).
### Logical Breakdown
For three sides $x$, $y$, and $z$ to be valid, all three of these conditions must be TRUE:
1. `x + y > z`
2. `y + z > x`
3. `z + x > y`

Why use `CASE`?

The `CASE` statement acts like an `if-else` block in traditional programming.
- WHEN: Checks if all three conditions are met using the `AND` operator.
- THEN: If all are true, it assigns the value '`Yes`'.
- ELSE: If any single condition fails, it defaults to '`No`'.
