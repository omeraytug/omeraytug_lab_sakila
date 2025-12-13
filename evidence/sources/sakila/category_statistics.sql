SELECT
    c.name AS category,
    ROUND(AVG(f.length), 2) AS avg_length
FROM
    staging.film AS f
    JOIN staging.film_category AS fc USING (film_id)
    JOIN staging.category AS c USING (category_id)
GROUP BY
    category
ORDER BY
    avg_length DESC;