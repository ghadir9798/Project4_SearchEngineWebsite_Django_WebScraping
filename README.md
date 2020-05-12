# Project4_SearchEngineWebsite_Django_WebScraping
 A Search Website using Django and Python WebScraping

 ### In order to run the Craigslist App on Docker please do the following:
 1. docker-compose build
 2. docker-compose up
 3. The app would be available on this address: 127.0.0.1:8000

 ### For creating a superuser or migrate the data, while you're in docker container, use these commands:
 - docker-compose run --rm python python manage.py createsuperuser
 - docker-compose run --rm python python manage.py makemigrations
 - docker-compose run --rm python python manage.py migrate


