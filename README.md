# Wagtail Secret Sharing

This add-on uses the [django-secret-sharing](https://github.com/vicktornl/django-secret-sharing) app.

## Features

- ...

## Requirements

- Python 3
- Django >= 2
- Wagtail >= 2

## Installation

Install the package

```
pip install wagtail-secret-sharing
```

Add `wagtail.contrib.routable_page` and `wagtail_secret_sharing` to your INSTALLED_APPS

INSTALLED_APPS = [
    ...
    "wagtail.contrib.routable_page",
    "wagtail_secret_sharing",
]


Extend the `AbstractSecretsPage`

```python
from wagtail_secret_sharing.models import AbstractSecretsPage

class SecretsPage(AbstractSecretsPage):
    template_name = "secrets.html"
```

Run migrate

```
python manage.py migrate
```

## Customization

Override the default templates with your own

```
{% extends "django_secret_sharing/secrets.html" %}

...
```

Note: for the landing page `_landing` is added to the `template_name`, if you want to change this override the `get_landing_page_template` method.
