--  delete all duplicate emails, keeping only one unique email with the smallest id.
WITH email_cte AS (
    SELECT
        id,
        email,
        ROW_NUMBER() OVER (
            PARTITION BY email
            ORDER BY id
        ) AS rn
    FROM Person
)
DELETE FROM email_cte
WHERE rn > 1;
