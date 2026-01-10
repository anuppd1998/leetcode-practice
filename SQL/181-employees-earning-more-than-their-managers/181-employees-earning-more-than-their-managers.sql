-- LeetCode 181: Employees Earning More Than Their Managers
-- Pattern: Self Join

CREATE TABLE Employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    salary INT,
    managerId INT
);

INSERT INTO Employee (id, name, salary, managerId) VALUES
(1, 'Joe',   70000, 3),
(2, 'Henry', 80000, 4),
(3, 'Sam',   60000, NULL),
(4, 'Max',   90000, NULL);

SELECT * FROM Employee;

SELECT
    e1.name AS Employee
FROM Employee e1
JOIN Employee e2 ON e2.id = e1.managerId
WHERE e1.salary > e2.salary;