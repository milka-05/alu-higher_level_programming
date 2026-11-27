# SQL_introduction

Introduction to MySQL queries and scripts.

| File | Description |
|------|-------------|
| `0-list_databases.sql` | Lists all databases of the MySQL server |
| `1-create_database_if_missing.sql` | Creates the database `hbtn_0c_0` if it does not already exist |
| `2-remove_database.sql` | Deletes the database `hbtn_0c_0` if it exists |
| `3-list_tables.sql` | Lists all tables of a database passed as an argument to `mysql` |
| `4-first_table.sql` | Creates a table called `first_table` in the current database if it does not exist |
| `5-full_table.sql` | Prints the full description of `first_table` from the database passed as an argument |
| `6-list_values.sql` | Lists all rows and fields of `first_table` from the database passed as an argument |
| `7-insert_value.sql` | Inserts a new row (`id = 89`, `name = Best School`) into `first_table` |
| `8-count_89.sql` | Displays the number of records with `id = 89` in `first_table` |
| `9-full_creation.sql` | Creates `second_table` and inserts four initial rows |
| `10-top_score.sql` | Lists `score` and `name` from `second_table` ordered by highest score first |
| `11-best_score.sql` | Lists `score` and `name` from `second_table` with `score >= 10` ordered by highest score first |
| `12-no_cheating.sql` | Updates `Bob` score to `10` in `second_table` using the `name` field |
| `13-change_class.sql` | Removes all records with `score <= 5` from `second_table` |
| `14-average.sql` | Computes the score average of all records in `second_table` |
| `15-groups.sql` | Lists the number of records with the same `score` in `second_table` sorted by count descending |
| `16-no_link.sql` | Lists `score` and `name` from `second_table` for rows with a name, ordered by score descending |
