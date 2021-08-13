select name from Employee e where salary > (select salary from Employee where id=e.manager_id);
--select e1.name from Employee e1 left join Employee e2 on e1.manager_id=e2.id where e1.salary>e2.salary;
