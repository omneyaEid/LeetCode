# Write your MySQL query statement below

select employee_id , 
        salary * ( employee_id%2)
        * ( name not like 'M%') 
        as  bonus
from Employees
order by employee_id


# another solution 

 select employee_id , 
   case when 
          employee_id%2 <>0 and name not like 'M%' 
    then salary 
   else 0
   end 
   as bonus
   from employees
   order by employee_id;


