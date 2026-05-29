# Write your MySQL query statement below
SELECT 
    CASE 
        -- If ID is odd and it is the last row, keep it the same
        WHEN id % 2 != 0 AND id = (SELECT COUNT(*) FROM Seat) THEN id
        -- If ID is odd and not the last row, increment it
        WHEN id % 2 != 0 THEN id + 1
        -- If ID is even, decrement it
        ELSE id - 1
    END AS id,
    student
FROM 
    Seat
ORDER BY 
    id ASC;