USE sakila;

#How many copies of the film Hunchback Impossible exist in the inventory system?
set @withSymbol := (select count(film_id) from inventory);
select @withSymbol;