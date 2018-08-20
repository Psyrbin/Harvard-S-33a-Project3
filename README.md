# Project 3
Templates:
register.html contains registration form;
login.html contains login page;
user.html contains menu, links to cart and orders and, if user is admin, link to the list of orders placed by all users;
add_special.html contains a form that allows users to specify what they want their special pizza to be;
add_toppings.html contains a list of all toppings and allows user to select them;
add_sub.html contais all additions available for selected sub;
cart.html contains all items selected by the user and allows to delete them or place an order;
orders.html contains a list of all orders placed by the user;
all_orders.html is only accessible by admins and contains list of orders placed by all users;
order.html contains a list of items in the order and allows admin to mark order as complete.

On the menu page when selecting a pizza with one or more toppings, users are redirected to the page when they can select toppings; when selecting a sub, users are redirected to the page when they can select additions that are available for this sub. When selecting any other item, it gets added to the cart.
My personal touch is allowing site administrators to mark orders as complete and allowing users to see the status of their pending or completed orders.

Superuser credentials:
login: admin
password: notcommon