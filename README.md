# python-lab
Python Lab

Executar os comandos abaixo:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Acessar http://127.0.0.1:8000/api/ para ver as apis criadas

APIs disponíveis (pode ser acessado e testado pelo browser):
http://127.0.0.1:8000/api/customers/
http://127.0.0.1:8000/api/customers/{id}/books
http://127.0.0.1:8000/api/books/
http://127.0.0.1:8000/api/books/{id}


API para reservar livro:
Endpoint: http://127.0.0.1:8000/api/books/{id}/reserve
Método: POST
Body: {"customer":{id}
