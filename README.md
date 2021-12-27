# store-your-books
This project allows to store your book list and manage them

## Run Locally
- git clone https://github.com/koksalkapucuoglu/store-your-books-api.git
- Run -> docker-compose run app sh -c "python manage.py test && flake8"
- Run -> docker-compose up
- Open a new shell and Run -> docker-compose run app sh -c "python manage.py createsuperuser"
- Open browser and go to 'http://127.0.0.1:8000/admin/login/?next=/admin/'
