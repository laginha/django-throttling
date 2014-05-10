django-throttling
=================

Throttling system for Django views.

```python
@throttle(number_of_requests=1)
def view(request):
    return HttpResponse('success')
```

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
    