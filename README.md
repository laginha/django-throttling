django-throttling
=================

Throttling system for Django views.

```python
@throttle(number_of_request=1)
def view(request):
    return HttpResponse('success')
```

It is possible to throttle

- each user
- by role
- by group
- by a "pool" of request of all anonymous users
- by a "pool" of request of all users
- by a "pool" of requests of all users in a group
- for group of views (scope)
