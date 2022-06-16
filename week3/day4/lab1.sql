USE sakila;

# 1. In the table actor, what last names are not repeated?
select last_name from actor where ((select count(last_name) from actor)) <= 1;

#2. Which last names appear more than once?
select last_name from actor where ((select count(last_name) from actor)) > 1;

#3. Using the rental table, find out how many rentals were processed by each employee.
select count(rental_id),staff_id from rental group by staff_id;

#4. Using the film table, find out how many films there are of each rating.
select rating, count(film_id) from film group by rating;

#5. What is the mean length of the film for each rating type. Round off the average lengths to two decimal places;
select rating, round(avg(length),2) as mean_length from film group by rating;

#6. Which kind of movies (rating) have a mean duration of more than two hours?
select rating, round(avg(length),2) > 120 as mean_length from film group by rating;

