# Employees Earning More Than Their Managers (LeetCode 181)

## Problem Statement

Given a table `Employee`, find the names of employees who earn more than their managers.

### Table Structure

| Column Name | Type |
|-------------|------|
| id          | int  |
| name        | varchar |
| salary      | int |
| managerId   | int |

`managerId` refers to the `id` of another employee.

---

## Example

Input:

| id | name  | salary | managerId |
|----|-------|--------|-----------|
| 1  | Joe   | 70000  | 3 |
| 2  | Henry | 80000  | 4 |
| 3  | Sam   | 60000  | NULL |
| 4  | Max   | 90000  | NULL |

Output:

| Employee |
|----------|
| Joe      |

---

## Approach

This problem is solved using a **self join**:

- Join the `Employee` table with itself.
- One instance represents the employee.
- The other represents the manager.
- Compare their salaries.

---
