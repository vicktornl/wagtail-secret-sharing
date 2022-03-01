# Wagtail Secret Sharing

[![Version](https://img.shields.io/pypi/v/wagtail-secret-sharing.svg?style=flat)](https://pypi.python.org/pypi/wagtail-secret-sharing/)
![CI](https://github.com/vicktornl/wagtail-secret-sharing/actions/workflows/ci.yml/badge.svg)

A secure sharing app for Wagtail using [django-secret-sharing](https://github.com/vicktornl/django-secret-sharing).

## Features

* Keep sensitive information out of your chat logs and email via a secure sharing protocol
* REST API
* One time secrets

## Requirements

- Python 3
- Django >= 2.2.8
- Wagtail >= 2

## Installation

Install the package

```
pip install wagtail-secret-sharing
```

Add `wagtail.contrib.routable_page`, `django_secret_sharing` and `wagtail_secret_sharing` to your INSTALLED_APPS

```
INSTALLED_APPS = [
    ...
    "wagtail.contrib.routable_page",
    "django_secret_sharing,
    "wagtail_secret_sharing",
]
```


Extend the `AbstractSecretsPage`

```python
from wagtail_secret_sharing.models import AbstractSecretsPage

class SecretsPage(AbstractSecretsPage):
    ...
```

Run migrate

```
python manage.py migrate
```

## Templates

Override the default templates with your own

**wagtail_secret_sharing/create.html**

```
{% load wagtailroutablepage_tags %}

{% if secret_url %}
    <p>{{ secret_url }}</p>
    <a href="{% routablepageurl page 'create' %}">Create</a>
{% else %}
  <form action="{% routablepageurl page 'create' %}" method="post">
      {% csrf_token %}
      {{ form }}
      <input type="submit" value="Submit">
  </form>
{% endif %}
```

**wagtail_secret_sharing/retrieve.html**

```
{% load wagtailroutablepage_tags %}

<a href="{% routablepageurl page 'view' url_part %}">View</a>
```

**wagtail_secret_sharing/view.html**

```
{% load wagtailroutablepage_tags %}

<textarea disabled>{{ value }}</textarea>
<a href="{% routablepageurl page 'create' %}">Create</a>
```
