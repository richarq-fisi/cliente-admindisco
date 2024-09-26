# Install
```sh
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
```

# MIGRATIONS
```sh
python manage.py makemigrations
python manage.py migrate
```

# SUPERUSER
```sh
python manage.py createsuperuser
root : toor
```

# RUN SERVER
```sh
python manage.py runserver
```



## Add Item
```
./templates/unfold/helpers/add_link.html:12:    <div class="flex flex-row items-center">
```