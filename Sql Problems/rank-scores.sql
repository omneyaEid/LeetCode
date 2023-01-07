# Write your MySQL query statement below

select score ,
        DENSE_RANK() OVER (
        ORDER BY
        scores_rank.score DESC
    ) AS 'rank'
from Scores scores_rank
order by score desc
