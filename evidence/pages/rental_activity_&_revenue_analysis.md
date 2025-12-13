# Rental Activity & Revenue Analysis

## Revenue Analysis

This section focuses on revenue patterns derived from customer payments.

### Monthly Revenue

```sql monthly_payment
select
  strftime(date_trunc('month', payment_date), '%Y, %B') as month,
  sum(amount) as revenue
from sakila.payment
group by month
order by month;

```

<BarChart
data={monthly_payment}
title="Revenue by month"
x=month
y=revenue
xType=category
colorPalette={[
'768948'
]}
/>

## Rental Activity Analysis

This section explores how rental activity evolves over time.

### Monthly Rentals

```sql monthly_rentals
select
    strftime(date_trunc('month', rental_date), '%Y, %B') as month,
    count(*) as rentals
from sakila.rental
group by 1
order by 1;
```

<BarChart
data={monthly_rentals}
title="Rentals by month"
x=month
y=rentals
xType=category
colorPalette={[
'768948'
]}  
/>

## Performance Based on Films

This section explores top performing movies.

### Top 10 Performing Movies (Total Revenue)

```sql top_movies
  SELECT
        f.title,
        SUM(p.amount) AS total_revenue
    FROM sakila.payment AS p
    JOIN sakila.rental AS r USING (rental_id)
    JOIN sakila.inventory AS i USING (inventory_id)
    JOIN sakila.film AS f USING (film_id)
    GROUP BY f.title
    ORDER BY total_revenue DESC
    LIMIT 10;
```

<BarChart
data={top_movies}
x=title
y=total_revenue
swapXY=true
colorPalette={[
'768948'
]}
/>

### Last 10 Performing Movies (Total Revenue)

```sql worst_movies
  SELECT
        f.title,
        SUM(p.amount) AS total_revenue
    FROM sakila.payment AS p
    JOIN sakila.rental AS r USING (rental_id)
    JOIN sakila.inventory AS i USING (inventory_id)
    JOIN sakila.film AS f USING (film_id)
    GROUP BY f.title
    ORDER BY total_revenue
    LIMIT 10;
```

<BarChart
data={worst_movies}
x=title
y=total_revenue
swapXY=true
colorPalette={[
'768948'
]}
/>

## Customer Analysis

This section explores customer spending behavior.

### Top Customers by Total Spend

```sql top_customer_spend
SELECT
  c.first_name || ' ' || c.last_name AS customer,
  SUM(p.amount) AS total_spend
FROM sakila.payment p
JOIN sakila.customer c USING (customer_id)
GROUP BY 1
ORDER BY total_spend DESC
LIMIT 10;
```

<DataTable data={top_customer_spend}/>

### Top Customers by Total Spend

```sql worst_customer_spend
SELECT
  c.first_name || ' ' || c.last_name AS customer,
  SUM(p.amount) AS total_spend
FROM sakila.payment p
JOIN sakila.customer c USING (customer_id)
GROUP BY 1
ORDER BY total_spend
LIMIT 10;
```

<DataTable data={worst_customer_spend}/>
