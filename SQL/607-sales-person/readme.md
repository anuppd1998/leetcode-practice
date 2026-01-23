# Sales Person (LeetCode Problem 607)
## Problem Statement
Table: `SalesPerson`
```
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| sales_id        | int     |
| name            | varchar |
| salary          | int     |
| commission_rate | int     |
| hire_date       | date    |
+-----------------+---------+
sales_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a salesperson alongside their salary, commission rate, and hire date.
 ```

Table: `Company`
```
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+
com_id is the primary key (column with unique values) for this table.
Each row of this table indicates the name and the ID of a company and the city in which the company is located.
 ```

Table: `Orders`
```
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+
order_id is the primary key (column with unique values) for this table.
com_id is a foreign key (reference column) to com_id from the Company table.
sales_id is a foreign key (reference column) to sales_id from the SalesPerson table.
Each row of this table contains information about one order. This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.
 ```

Write a solution to find the names of all the salespersons who did not have any orders related to the company with the name "RED".

Return the result table in any order.

The result format is in the following example.

 

### Example 1:
```
Input: 
SalesPerson table:
+----------+------+--------+-----------------+------------+
| sales_id | name | salary | commission_rate | hire_date  |
+----------+------+--------+-----------------+------------+
| 1        | John | 100000 | 6               | 4/1/2006   |
| 2        | Amy  | 12000  | 5               | 5/1/2010   |
| 3        | Mark | 65000  | 12              | 12/25/2008 |
| 4        | Pam  | 25000  | 25              | 1/1/2005   |
| 5        | Alex | 5000   | 10              | 2/3/2007   |
+----------+------+--------+-----------------+------------+
Company table:
+--------+--------+----------+
| com_id | name   | city     |
+--------+--------+----------+
| 1      | RED    | Boston   |
| 2      | ORANGE | New York |
| 3      | YELLOW | Boston   |
| 4      | GREEN  | Austin   |
+--------+--------+----------+
Orders table:
+----------+------------+--------+----------+--------+
| order_id | order_date | com_id | sales_id | amount |
+----------+------------+--------+----------+--------+
| 1        | 1/1/2014   | 3      | 4        | 10000  |
| 2        | 2/1/2014   | 4      | 5        | 5000   |
| 3        | 3/1/2014   | 1      | 1        | 50000  |
| 4        | 4/1/2014   | 1      | 4        | 25000  |
+----------+------------+--------+----------+--------+
Output: 
+------+
| name |
+------+
| Amy  |
| Mark |
| Alex |
+------+
Explanation: 
According to orders 3 and 4 in the Orders table, it is easy to tell that only salesperson John and Pam have sales to company RED, so we report all the other names in the table salesperson.
```
## Approach - 1
1. *Map the Relationships (*`sales_cte`*)*: We start with a `LEFT JOIN` between `SalesPerson` and `Orders`. This ensures we keep every salesperson, even if they have zero orders. We then join `Company` to see which company each order belongs to.

2. *Identify the "RED" Sellers (*`company_cte`*)*: We filter our first CTE to create a specific list of names who have at least one record associated with 'RED'.

3. *The Exclusion Filter (*`NOT IN`*)*: In the final `SELECT`, we go back to our full list of salespeople. The `WHERE ... NOT IN` clause acts as a filter that removes anyone whose name appeared in the "RED" list.

4. *Deduplication*: We use `DISTINCT` to ensure each name appears only once, as a salesperson might have multiple orders for other companies.

## Approach - 2
1. *Iterative Selection*: The outer query starts scanning the `SalesPerson` table row by row.

2. *Correlated Lookup*: For every single salesperson (e.g., "John"), the subquery "reaches out" to the `Orders` and `Company` tables to see if there is a match where the sales_id is John's and the company name is 'RED'.

3. *Existence Check*:

    - If the subquery finds at least one row (the "1" in `SELECT 1`), the `EXISTS` condition becomes true.
    - Since we use `NOT EXISTS`, that salesperson is excluded from the final results.

4. *Handling Non-Sellers*: If a salesperson has no orders at all (like Amy or Mark), the subquery returns nothing. `NOT EXISTS` sees this empty result as "True," so they are correctly included in the final list.