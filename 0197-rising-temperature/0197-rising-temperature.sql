# Write your MySQL query statement below


SELECT W1.id
From
    Weather W1
JOIN
    Weather W2
ON 
    dateDiff(W1.recordDate, W2.recordDate) = 1
WHERE
    W1.temperature > W2.temperature

-- Using Cartesian Product 
-- SELECT W1.id
-- FROM 
--     Weather W1, Weather W2
-- Where dateDiff(W1.recordDate, W2.recordDate) = 1 And W1.temperature > W2.temperature