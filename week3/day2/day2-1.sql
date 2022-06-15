USE sakila;
#1. Which actor has appeared in the most films?
SELECT a.first_name, a.last_name, count(b.film_id) as num_appearances
FROM actor a
JOIN film_actor b
USING (actor_id)
GROUP BY b.actor_id
ORDER BY num_appearances desc
LIMIT 1;

#2. Most active customer (the customer that has rented the most number of films)
SELECT a.first_name, a.last_name, count(b.customer_id) as num_rental
FROM customer a
JOIN rental b
USING (customer_id)
GROUP BY b.customer_id
ORDER BY num_rental desc
LIMIT 1;

#3.List number of films per category.
SELECT a.name, count(b.category_id) as category_count
FROM category a
JOIN film_category b
USING (category_id)
GROUP BY b.category_id,a.name
ORDER BY name;

#4. Display the first and last names, as well as the address, of each staff member.
SELECT a.first_name, a.last_name, b.address as staff_address
from staff a
join address b
using(address_id);
#group by address_id;

#5. Display the total amount rung up by each staff member in August of 2005.
SELECT a.first_name, a.last_name, sum(b.amount) as total_sale 
from staff a 
join payment b 
using(staff_id)
where year(payment_date) = 2005 and month(payment_date) = 08
group by staff_id;

#6. List each film and the number of actors who are listed for that film.
SELECT a.title, count(b.actor_id) as actor_count
from film a
left join film_actor b
using(film_id)
group by title
ORDER BY actor_count desc;

# 7. Using the tables payment and customer and the JOIN command,
# optional. list the total paid by each customer. List the customers alphabetically by last name.
SELECT a.first_name, a.last_name, sum(b.amount) as total_purchase
from customer a
join payment b
using(customer_id)
group by customer_id;

#Optional. Which is the most rented film? The answer is Bucket Brotherhood This query might require using more than one join statement. Give it a try.
select f.title, count(f.title) from film as f inner join (inventory as i) using (film_id)
inner join (rental as r) using (inventory_id)
group by title
order by count(title) desc
limit 1