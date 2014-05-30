# Settings

## THROTTLING_STATUS\_CODE

The response's status code in case the user gets throttled. Defaults to `429`.

```python
THROTTLING_STATUS_CODE = 403
```

## THROTTLING_INTERVAL

Time in minutes to reset throttling. Defaults to `1440` minutes (one day).

```python
THROTTLING_INTERVAL = 60
```

## THROTTLING\_NUMBER\_OF_REQUESTS

The default maximum number of requests after which the user is throttled. Defaults to `1000`.

```python
THROTTLING_NUMBER_OF_REQUESTS = 10000
```

## THROTTLING_CONFIG

Pre-defined configurations for throttling views. Defaults to `{}`

```python
THROTTLING_CONFIG = {
    "anonymous": {
        "number_of_requests": 1000,
        "per_anonymous": True,
    }
}
```

```python
@throttle(config="anonymous")
def someview(requests):
    return HttpResponse('success')

'''which is the same as'''

@throttle(number_of_requests=1000, per_anonymous=True)
def someview(requests):
    return HttpResponse('success')
```
