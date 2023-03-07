<h1>API de Agenda</h1>

Status: Developing ⚠️

### API created to store information about schedules, courts, locations, payments, and so on...

## The libraries used are:

+ asgiref==3.6.0
+ Django==4.1.7
+ djangorestframework==3.14.0
+ Markdown==3.4.1
+ pytz==2022.7.1
+ sqlparse==0.4.3
+ tzdata==2022.7

## The API has the following routes:

+ GET /company/ - returns all registered companies
+ POST /company/ - creates a new company
+ GET /company/:id - returns a specific company
+ PUT /company/:id - updates a specific company
+ DELETE /company/:id - deletes a specific company
+ GET /customer/ - returns all registered customers
+ POST /customer/ - creates a new customer
+ GET /customer/:id - returns a specific customer
+ PUT /customer/:id - updates a specific customer
+ DELETE /customer/:id - deletes a specific customer
+ GET /place/ - returns all available courts/fields
+ POST /place/ - creates a new court/field
+ GET /place/:id - returns a specific court/field
+ PUT /place/:id - updates a specific court/field
+ DELETE /place/:id - deletes a specific court/field
+ GET /payment/ - returns all registered payment types
+ POST /payment/ - creates a new payment type
+ GET /payment/:id - returns a specific payment type
+ PUT /payment/:id - updates a specific payment type
+ DELETE /payment/:id - deletes a specific payment type
+ GET /scheduling/ - returns all scheduled times
+ POST /scheduling/ - creates a new scheduling
+ GET /scheduling/:id - returns a specific scheduling
+ PUT /scheduling/:id - updates a specific scheduling
+ DELETE /scheduling/:id - deletes a specific scheduling
+ GET /customer/:id/horarios - returns all scheduled times for a specific customer
For each resource, the API supports CRUD operations (Create, Read, Update, and Delete). In addition, there is a route to list the scheduled times for a specific customer.

## The models used are:

+ Company: represents the location where the courts/fields are located
+ Customer: represents the customers who book schedules
+ Place: represents each available court/field at each location
+ Payment: represents the accepted payment methods for each booking
+ Scheduling: represents each scheduled time booking for a specific court/field by a specific customer.

## The serializers used are:

+ CompanySerializer: serializes/deserializes Company objects
+ CustomerSerializer: serializes/deserializes Customer objects
+ PlaceSerializer: serializes/deserializes Place objects
+ PaymentSerializer: serializes/deserializes Payment objects
+ SchedulingSerializer: serializes/deserializes Scheduling objects
+ HorariosClientesSerializer: serializes/deserializes scheduling times for specific customers



## To run the API, follow these steps:

## Install the VENV
	py -m venv env
	
## Activate venv for windows
	.\env\Scripts\activate

## Install the required libraries:
	pip install -r requirements.txt

## Run the database migrations:
	python manage.py migrate
	python manage.py makemigrations
	
## Start server:
	python manage.py runserver


Informações adicionais:

Versão da API: 1.0.0
Autor: [Henrique Santos]
