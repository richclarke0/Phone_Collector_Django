# Phones Django Project

This guide assumes you have Python, Django and Postgres installed already.

### *Step by step guide:*

Use a commend installed with PostgreSQL to create the database for our project, titled *phones*.

```$ createdb phones```

now: ``cd phones``

Now we have this:
>Phones/
>>Phones/
>>>__init.py

>>>etc

>>>settings.py

>>>urls.py

Check INSTALLED_APPSlist in catcollector/settings.py. Those pre-installed apps provide services such as the admin app and the ability to serve static files.

You need a ``main_app`` to implement functionality. Run this command:

```python3 manage.py startapp main_app```

Now include it in ``INSTALLED_APPS`` by doing this:
```
INSTALLED_APPS = [ 
    'main_app',
	'django.contrib.admin',   etc
```

and then run the server ``python3 manage.py runserver``

navigate to server localhost:8000 and you'll see the rocketship splash page

### Now add the database:
In ``settings.py``
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'phones',
    }
}
```