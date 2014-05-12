# Usage

## Get ready

Firstly you need to add to your project's settings

```python
INSTALLED_APPS = (
    ...
    'throttling',
    'userroles', #optional
)
```

Don't forget to sync it.

## Meet the decorator

```python
@throttle()
def view(request):
    return HttpResponse('success')
```

This will limit each user (anonymous or authenticated) to a default maximum number of requests for this specific view.


### Args

#### number_of\_requests

Defines the maximum number of requests a user our group of users is allowed for a specific view. Defaults to `THROTTLING_NUMBER_OF_REQUESTS` setting.

```python
@throttle(number_of_requests=100)
def view(request):
    return HttpResponse('success')
```

or just

```python
@throttle(100)
def view(request):
    return HttpResponse('success')
```

#### all_users

Limit all user (anonymous or authenticated) to a shared maximum number of requests for a specific view. In other words, all users, together, are limited to a given `number_of_requests`.

```python
@throttle(100, all_users=True)
def view(request):
    return HttpResponse('success')
```

#### per_anonymous

Limit each anonymous user to a maximum number of requests for a specific view.

```python
@throttle(100, per_anonymous=True)
def view(request):
    return HttpResponse('success')
```

#### all_anonymous

Limit all anonymous user to a shared maximum number of requests for a specific view. In other words, all anonymous users, together, are limited to a given `number_of_requests`.

```python
@throttle(100, all_anonymous=True)
def view(request):
    return HttpResponse('success')
```

#### role

Limit each authenticated user with a certain `userrole`, to a maximum number of requests for a specific view.

```python
@throttle(100, role='developer')
def view(request):
    return HttpResponse('success')
```

You need to add `"userroles"` to `INSTALLED_APPS` and add `USER_ROLES` to your settings file.

```python
USER_ROLES = (
    'other',
    'developer',
)
```

For more information, go [here](https://github.com/laginha/django-user-roles/)

#### all_with\_role

ToDo

#### group

Limit each authenticated user that bellongs to a `Group` (`django.contrib.auth.models`), to a maximum number of requests for a specific view.

```python
@throttle(100, group='somegroup')
def view(request):
    return HttpResponse('success')
``` 

#### all_in\_group

Limit all authenticated users that bellong to a `Group` (`django.contrib.auth.models`), to a shared maximum number of requests for a specific view. In other words, each group is limited to a given `number_of_requests`.

```python
@throttle(100, all_users=True)
def view(request):
    return HttpResponse('success')
```

#### scope

The scope in which the view is in. This allows to group views together, thus each view in a scope shares the limits regarding the number of requests.

```python
@throttle(100, scope="developer")
def view(request):
    return HttpResponse('success')
```

#### settings

The key for the `THROTTLING_OPTIONS` setting. Check the [settings documentation](settings.md#throttling_options).

```python
@throttle(setting="developer")
def view(request):
    return HttpResponse('success')
```

#### interval

Defines the time in minutes after which the throttling is reset. Defaults to `THROTTLING_INTERVAL` setting. Check the [settings documentation](settings.md#throttling_interval).

```python
@throttle(100, interval=60)
def view(request):
    return HttpResponse('success')
```
