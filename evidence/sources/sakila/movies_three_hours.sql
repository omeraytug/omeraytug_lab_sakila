select
    title,
    length
from
    staging.film
where
    length > 180
order by
    length;