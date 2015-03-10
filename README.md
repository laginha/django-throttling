django-throttling
=================

Throttling system for Django views.

## Install

    pip install throttling

## Basic Usage

Add to settings

```python
INSTALLED_APPS = (
    ...
    'throttling',
)
```

and in your views

```python
from throttling.decorators import throttle

@throttle(1000)
def view(request):
    return HttpResponse('success')
```

Check the [docs](docs/index.md)

## features

- limit to a maximum number of requests for each view or for a group of views
    - each anonymous user
    - each user (anonymous or authenticated)
    - each authenticated user with a certain user role
    - each authenticated user that bellongs to a group
- limit to a shared maximum number of requests for each view or for a group of views
    - all anonymous users
    - all users (anonymous or authenticated)
    - all authenticated users that bellong to a group
    