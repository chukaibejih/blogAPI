# Blog API

A Blog API using the full set of Django REST Framework features.
It has users, permissions, and allow for full CRUD (Create-Read-Update-Delete) functionality.

## Installation

Create a virtual environment.

```bash
pip install Django
```
```bash
pip install djangorestframework
```


## Usage

Add rest_framework to INSTALLED_APPS

```python
INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
# 3rd-party apps
'rest_framework', # new
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
