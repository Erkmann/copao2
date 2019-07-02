# copao2


## Como usar

Crie uma virtualenv e instale as dependências com o pip:

```
pip install -r requirements.txt
```

### Modo de desenvolvimento

O modo de desenvolvimento utiliza um arquivo SQLite como banco dados,
e por isso não requer qualquer configuração.

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### Modo de produção

O modo de produção requer um banco de dados PostgreSQL.

Escolha uma _secret key_ de pelo menos 32 caracteres.

```
export DJANGO_ENV=production
export SECRET_KEY=changeme
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
