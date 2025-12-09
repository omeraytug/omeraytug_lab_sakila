```sql films
from sakila.film;

```

```sql movies_longer_than_180_mins
from sakila.movies_three_hours;

```

<BarChart
    data={movies_longer_than_180_mins}
    title="Movies longer than 180 mins, {inputs.category.label}"
    x=title
    y=length
    xAxisTitle="Movie title"
    yAxisTitle="Length"
/>
