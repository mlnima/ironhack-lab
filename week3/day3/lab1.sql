USE sakila;
#1. How many copies of the film Hunchback Impossible exist in the inventory system?
set @hunchBackImpossibleId := (select film_id from sakila.film where title = 'HUNCHBACK IMPOSSIBLE');
select count(film_id) from sakila.inventory where film_id = @hunchBackImpossibleId;

#2. List all films whose length is longer than the average of all the films.
set @averageOfAllFilms := (select round(avg(length),2) from film);
select * from film where length > @averageOfAllFilms;

#3. Use subqueries to display all actors who appear in the film ALONE TRIP.
set @alonTripFilmId := (select film_id from sakila.film where title = 'ALONE TRIP');
select first_name, last_name from actor where actor_id in (select actor_id from film_actor where film_id = @alonTripFilmId);

#4 .Sales have been lagging among young families, and you wish to target all family movies for a promotion.
# Identify all movies categorized as family films.
set @familyCategoryId := (select category_id from sakila.category where name = 'Family');
select * from film where film_id in (select film_id from film_category where category_id = @familyCategoryId);

#Get name and email from customers from Canada using subqueries.
#Do the same with joins. Note that to create a join, you will have to identify the correct tables with their primary keys and foreign keys,
#that will help you get the relevant information.
set @canadaId := (select country_id from sakila.country where country = 'Canada');
select first_name, last_name, email from customer 
where address_id in (
	select address_id from address 
	where city_id in (
		select city_id from city 
		where country_id = @canadaId
	)
);


set @canadaId := (select country_id from sakila.country where country = 'Canada');
select first_name, last_name, email from customer 
where address_id in (
	select address_id from address 
	where city_id in (
		select city_id from city 
		where country_id = @canadaId
	)
);
