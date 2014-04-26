Summary: 
########
“Ferris wheel” application is created using Django framework, which contains server and client side logic.

Server side logic: 
#################
It exposes a Django view that generates a set of 9 random integers, 9 digits in length, and returns that set to the client.  Every request from the client results in a new set of integers.


Client side logic: 
##################
It renders a grid or table, containing 3 columns and 3 rows (9 cells total).  Each cell has background color set to an RGB value corresponding to the integer in a particular cell, retrieved from the server.  It includes a button that, when clicked, cycles the cell colors forward in a clockwise manner. It also includes a button which generates new set of values and corresponding colors.
