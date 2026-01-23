# Big Countries (LeetCode Problem 595)
## Problem Statement


Table: `World`
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
name is the primary key (column with unique values) for this table.
Each row of this table gives information about the name of a country, the continent to which it belongs, its area, the population, and its GDP value.
 ```

A country is big if:

- it has an area of at least three million (i.e., `3000000 km²`), or
- it has a population of at least twenty-five million (i.e., `25000000`).

Write a solution to find the name, population, and area of the big countries.

Return the result table in any order.

The result format is in the following example.

 

### Example 1:
```
Input: 
World table:
+-------------+-----------+---------+------------+--------------+
| name        | continent | area    | population | gdp          |
+-------------+-----------+---------+------------+--------------+
| Afghanistan | Asia      | 652230  | 25500100   | 20343000000  |
| Albania     | Europe    | 28748   | 2831741    | 12960000000  |
| Algeria     | Africa    | 2381741 | 37100000   | 188681000000 |
| Andorra     | Europe    | 468     | 78115      | 3712000000   |
| Angola      | Africa    | 1246700 | 20609294   | 100990000000 |
+-------------+-----------+---------+------------+--------------+
Output: 
+-------------+------------+---------+
| name        | population | area    |
+-------------+------------+---------+
| Afghanistan | 25500100   | 652230  |
| Algeria     | 37100000   | 2381741 |
+-------------+------------+---------+
```
## Approach
The core logic here uses the OR operator. In SQL, the `OR` operator ensures that a record is included in the final result if at least one of the conditions is met.

1. *Selection*: We target the three specific attributes required: `name`, `population`, and `area`.
2. *Size Threshold*: We filter for countries with a landmass of at least 3,000,000 $km^2$.
3. *Density Threshold*: We filter for countries with a population of at least 25,000,000 people.
4. *Logical Union*: By using `OR`, the database engine will return countries that are huge but sparsely populated (like Canada), countries that are small but very crowded, and countries that meet both criteria (like China or the USA).