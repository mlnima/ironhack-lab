# 3. Select one column from a table. Get film titles.
SELECT title FROM sakila.film;
# 4. Select one column from a table and alias it.
# 4. Get unique list of film languages under the alias language. Note that we are not asking you to obtain the language per each film, but this is a good time to think about how you might get that information in the future
SELECT distinct language_id as lang FROM sakila.film; 

#5.1 Find out how many stores does the company have?
select count(store_id) from sakila.store

#5.2 Find out how many employees staff does the company have?
select count(staff_id) from sakila.staff

#5.3 Return a list of employee first names only?
select staff_id,first_name from sakila.staff group by staff_id
