# SQL_more_queries

MySQL privileges, permissions, joins, and constraints.

| File | Description |
|------|-------------|
| `0-privileges.sql` | Lists all privileges of `user_0d_1` and `user_0d_2` on `localhost` |
| `1-create_user.sql` | Creates `user_0d_1` on `localhost` with password `user_0d_1_pwd` and all server privileges |
| `2-create_read_user.sql` | Creates database `hbtn_0d_2` and `user_0d_2` with `SELECT` privilege on `hbtn_0d_2` |
| `3-force_name.sql` | Creates the table `force_name` with a non-null `name` column |
| `4-never_empty.sql` | Creates the table `id_not_null` with `id` defaulting to `1` |
| `5-unique_id.sql` | Creates the table `unique_id` with a unique `id` column defaulting to `1` |
| `6-states.sql` | Creates database `hbtn_0d_usa` and table `states` with auto-increment primary key `id` |
| `7-cities.sql` | Creates database `hbtn_0d_usa` and table `cities` with a foreign key referencing `states(id)` |
| `8-cities_of_california_subquery.sql` | Lists all cities of California from `hbtn_0d_usa` sorted by `cities.id` ascending using a subquery |
| `9-cities_by_state_join.sql` | Lists all cities with their state names from `hbtn_0d_usa` sorted by `cities.id` ascending |
| `10-genre_id_by_show.sql` | Lists TV shows with their linked genre IDs, sorted by show title and genre ID |
| `11-genre_id_all_shows.sql` | Lists all TV shows and their genre IDs, including shows without genres using a LEFT JOIN |
| `12-no_genre.sql` | Lists all TV shows without a linked genre, sorted by title and genre ID |
| `13-count_shows_by_genre.sql` | Counts the number of TV shows linked to each genre, sorted by descending count |
| `14-my_genres.sql` | Lists all genres linked to the TV show Dexter, sorted alphabetically |
| `15-comedy_only.sql` | Lists all Comedy TV shows, sorted alphabetically by title |
| `16-shows_by_genre.sql` | Lists all TV shows with their genre names, including shows without genres, sorted by title and genre |
