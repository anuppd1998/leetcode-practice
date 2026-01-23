/* Approach: 
1. Create a master list of all salespeople and their associated companies.
2. Isolate the names of people who HAVE sold to 'RED'.
3. Return everyone from the master list who IS NOT in that 'RED' list.
*/

WITH sales_cte AS (
    SELECT
        sp.name AS SalesPerson_name,
        c.name AS Company_name
    FROM SalesPerson sp
    -- LEFT JOIN keeps salespeople even if they have no orders
    LEFT JOIN Orders o ON sp.sales_id = o.sales_id
    -- Link to Company to get the actual name ('RED', 'GREEN', etc.)
    LEFT JOIN Company c ON o.com_id = c.com_id
),
company_cte AS (
    -- Identify anyone who has at least one order with 'RED'
    SELECT
        SalesPerson_name
    FROM sales_cte
    WHERE Company_name = 'RED'
)

-- Final result: People who are NOT in the 'RED' list
SELECT
    DISTINCT SalesPerson_name AS name
FROM sales_cte
WHERE SalesPerson_name NOT IN (
    SELECT SalesPerson_name FROM company_cte
);

--------------------- 2nd Approach ------------------
/* Approach:
Use a correlated subquery with NOT EXISTS to filter out salespeople 
who have any association with the company 'RED'.
This is more efficient and NULL-safe than using 'NOT IN'.
*/

SELECT 
    name 
FROM 
    SalesPerson sp
WHERE 
    -- For each salesperson, check if the following condition is FALSE:
    NOT EXISTS (
        SELECT 1 
        FROM 
            Orders o
        -- Join Orders to Company to verify the company name
        JOIN 
            Company c ON o.com_id = c.com_id
        WHERE 
            -- Link the subquery to the current salesperson in the outer query
            o.sales_id = sp.sales_id 
            -- Specifically look for 'RED' company orders
            AND c.name = 'RED'
    );