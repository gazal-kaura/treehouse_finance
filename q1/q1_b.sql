SELECT AVG(salary) FROM Employee where id not in (Select manager_id from Employee where manager_id IS NOT NULL);
