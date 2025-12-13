# Film and Category Insights

This section analyzes Films & Categories.

## Revenue by Category

```sql revenue_category
SELECT
  c.name AS category,
  SUM(p.amount) AS revenue
FROM sakila.payment p
JOIN sakila.rental r USING (rental_id)
JOIN sakila.inventory i USING (inventory_id)
JOIN sakila.film_category fc USING (film_id)
JOIN sakila.category c USING (category_id)
GROUP BY 1
ORDER BY revenue DESC;
```

<BarChart
data={revenue_category}
title="Revenue by category"
x=category
y=revenue
xType=category
swapXY=true
colorPalette={[
'7b2cbf'
]}
/>

## Average Movie Length for each Category

```sql category_statistics
from sakila.category_statistics;

```

<BarChart
data={category_statistics}
x=category
y=avg_length
swapXY=true
colorPalette={[
'7b2cbf'
]}
/>

## Actors with most movies

```sql most_movies
 SELECT
        a.first_name || ' ' || a.last_name AS actor_name,
        COUNT(fa.film_id) AS movie_count
    FROM
        sakila.actor AS a
    JOIN
        sakila.film_actor AS fa
    ON
        a.actor_id = fa.actor_id
    GROUP BY
        actor_name
    ORDER BY
        movie_count DESC
    limit 10;
```

<BarChart
data={most_movies}
x=actor_name
y=movie_count
swapXY=true
colorPalette={[
'7b2cbf'
]}
/>
