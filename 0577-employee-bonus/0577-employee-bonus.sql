# Write your MySQL query statement below

SELECT name, bonus
FROM
    Employee emp
LEFT OUTER JOIN
    Bonus b
ON 
    b.empId = emp.empId
WHERE
    b.bonus < 1000 OR Bonus is NULL