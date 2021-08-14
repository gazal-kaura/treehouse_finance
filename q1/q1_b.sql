select avg(salary) FROM Employee where id not in (select manager_id from Employee where manager_id is not null);
