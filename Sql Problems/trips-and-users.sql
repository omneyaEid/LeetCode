# Write your MySQL query statement below

select trip.Request_at as Day, round(sum(case when trip.Status != 'completed' then 1 else 0 end)/count(*),2)
as 'Cancellation Rate'
from Trips trip
where trip.Client_Id in (select Users_Id from Users where Banned ='No')
and trip.Driver_Id in (select Users_Id from Users where Banned = 'No')
and trip.Request_at between '2013-10-01' and '2013-10-03'
group by trip.Request_at;