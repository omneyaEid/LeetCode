# Write your MySQL query statement below

select distinct
	S.id,
	S.visit_date,
	S.people
from
	Stadium S, (
	select
		S1.id as id1,
		S2.id as id2
	from
		Stadium S1, Stadium S2
	where
		S2.id - S1.id >= 2 and
		not exists (
			select S3.id
			from Stadium S3
			where
				S3.people < 100 and
				S3.id between S1.id and S2.id
		)
    ) S100
where
	S.id between S100.id1 and S100.id2
order by S.id