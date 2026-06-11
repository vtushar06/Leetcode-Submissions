CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  -- Adjust N to be 0-indexed for the OFFSET clause
  SET N = N - 1;
  
  RETURN (
      -- Write your MySQL query statement below.
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET N
  );
END