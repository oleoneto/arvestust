# Django Arvestust

**arvestust** is a django app file management and record-keeping.

![PyPI - License](https://img.shields.io/pypi/l/django-arvestust)
![PyPI - Version](https://img.shields.io/pypi/v/django-arvestust)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/django-arvestust)
![Github - Issues](https://img.shields.io/github/issues/lehvitus/arvestust)
![PyPI - Downloads](https://img.shields.io/pypi/dm/django-arvestust)

#### Dependencies
**arvestust** depends on django itself, [`django-crispy-forms`](https://pypi.org/project/django-crispy-forms/), and [`python-magic`](https://pypi.org/project/python-magic/).


#### Models
The app is split into three main models:
- [comment](arvestust/models/comment.py)
- [file](arvestust/models/file.py)
- [follow](arvestust/models/follow.py)
- [like](arvestust/models/like.py)
- [save](arvestust/models/save.py)
- [tag](arvestust/models/tag.py)


#### Installation
1. Add **arvestust** to your `INSTALLED_APPS` setting like this::
```python
    INSTALLED_APPS = [
        # other apps...
        'arvestust',
    ]
```

Alternatively, you can also add this app like so::
```python
    INSTALLED_APPS = [
        # other apps...
        'arvestust.apps.ArvestustConfig',
    ]
```

2. Include the polls URLconf in your project urls.py like this::
```python
    path('records/', include('arvestust.urls', namespace='arvestust')),
```

2.1. Optionally, you can also add the api endpoints in your project urls.py like so::
```python
    path('api/', include('arvestust.api', namespace='arvestust_api')),
```

3. Run ``python manage.py migrate`` to create the app models.

4. Start the development server and visit [`http://127.0.0.1:8000/admin/`](http://127.0.0.1:8000/admin/)
   to start a add chat groups and messages (you'll need the Admin app enabled).

5. Visit [`http://127.0.0.1:8000/records/`](http://127.0.0.1:8000/records/) to use the app.

5.1. If you've included the api urls as well, you can visit the endpoints by visiting:
```
    http://127.0.0.1:8000/api/...
```

## License
**arvestust** is [BSD-Licensed](LICENSE.md).

------

Built with [django-clite](https://github.com/oleoneto/django-clite).

Developed and maintained by [Leo Neto](https://github.com/oleoneto)
