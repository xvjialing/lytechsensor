#### first

- 安装Django
```
pip install django
```

- 安装Django REST framework

```
pip install djangorestframework
pip install markdown       # Markdown support for the browsable API.
pip install django-filter  # Filtering support

```


- 运行django

`python manage.py runserver 0.0.0.0:8088`

- 更新数据库
```
python manage.py makemigrations modelName

python manage.py migrate
```