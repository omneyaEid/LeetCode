# Write your MySQL query statement below

SELECT Department.Name AS Department,
       emp.Name AS Employee,
       emp.Salary AS Salary
FROM Department
JOIN Employee emp
ON Department.Id = emp.DepartmentId
WHERE emp.Salary =
(
    SELECT Max(Salary)
    FROM Employee emp2
    WHERE emp2.DepartmentId = emp.DepartmentId
)