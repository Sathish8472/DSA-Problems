# Write your MySQL query statement below
SELECT W1.id
FROM 
    Weather W1, Weather W2
Where dateDiff(W1.recordDate, W2.recordDate) = 1 And W1.temperature > W2.temperature