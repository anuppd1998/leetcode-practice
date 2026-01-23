/* Approach:
1. Use GROUP BY to consolidate all student records into their respective classes.
2. Use COUNT(*) to calculate the total number of students in each class.
3. Apply the HAVING clause to filter groups based on the calculated count.
*/

SELECT
    class
FROM Courses
-- Consolidate rows by class name
GROUP BY class
-- Filter out classes with fewer than 5 students
-- Note: HAVING is used here because WHERE cannot be used with aggregate functions
HAVING COUNT(*) >= 5;