# Welcome in this technical test documentation
______


The project is named lengowproject wow such inspiration. It is also the main app.

There are requirements and a .env file. I am running this program with Python 3.10.4

I used sqlite3 because you said it was ok.


Question 2: 
-
I took the liberty to select 4 simple fields and one object field to put a ForeignKey.

You will find those fields in *orders/models.py*


Question 3:
-

The command **create_orders_from_api** is available in *orders/management/commands*


Question 4:
-

I am actually not sure about this one if the thing was to create basic view or use directly
Django Rest Framework. I am more used to DRF so I chose this solution.

### How to test :

1. Run the django server
2. Navigate to /api/orders/ -> This route will list all orders present in your database
3. Want to search for one and only one order ? Navigate to /api/orders/{your_id} if the order 
is in the database you will only see this one. If it does not exist it will raise a 500.
4. Want to filter the order queryset by a specific field ? Navigate to /api/orders/ and add in the
url your filter for example /api/orders/?marketplace=amazon



Question 5 :
-

I added the format command which is basically running black on every file in the project.

It could be cool to add in this command or in another one ISort. 

To run this command : *./manage.py format*


Question 6:
-

Every view is already accessible by the API as I explained before in this document. The command
to create orders is also available here : /api/create_orders_from_api/



## Bonus :

There are some tests available in orders/tests.py. It is not complete but it is a start.
