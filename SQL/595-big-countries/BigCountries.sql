/* Approach: 
Find 'big' countries by evaluating two independent metrics.
A country is selected if it satisfies EITHER the area requirement 
OR the population requirement.
*/

SELECT
    name,
    population,
    area
FROM 
    World
WHERE 
    -- Criterion A: Large geographic footprint (3 million sq km or more)
    area >= 3000000
    
    -- Criterion B: Large human footprint (25 million people or more)
    OR population >= 25000000;