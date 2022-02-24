# Wagtail Secret Sharing

[![Version](https://img.shields.io/pypi/v/wagtail-secret-sharing.svg?style=flat)](https://pypi.python.org/pypi/wagtail-secret-sharing/)
![CI](https://github.com/vicktornl/wagtail-secret-sharing/actions/workflows/ci.yml/badge.svg)

A secure sharing app for Wagtail using [wagtail-secret-sharing](https://github.com/vicktornl/wagtail-secret-sharing).

## Features

* Keep sensitive information out of your chat logs and email via a secure sharing protocal
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

Add `wagtail.contrib.routable_page` and `wagtail_secret_sharing` to your INSTALLED_APPS

```
INSTALLED_APPS = [
    ...
    "wagtail.contrib.routable_page",
    "wagtail_secret_sharing",
]
```


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

## Templates

Override the default templates with your own

**django_secret_sharing/create.html**
**django_secret_sharing/retrieve.html**
**django_secret_sharing/view.html**
