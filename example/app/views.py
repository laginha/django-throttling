# Create your views here.
from django.http import HttpResponse
from throttling.decorators import throttle

def view_without_throttle(request):
    return HttpResponse('success')

@throttle()
def view_with_throttle(request):
    return HttpResponse('success')

@throttle(per_anonymous=True)
def view_with_throttle_per_anonymous(request):
    return HttpResponse('success')
    
@throttle(all_anonymous=True)
def view_with_throttle_all_anonymous(request):
    return HttpResponse('success')

@throttle(all_users=True)
def view_with_throttle_all_users(request):
    return HttpResponse('success')

@throttle(role='developer')
def view_with_throttle_role(request):
    return HttpResponse('success')
    
@throttle(group='groupname')
def view_with_throttle_group(request):
    return HttpResponse('success')
    
@throttle(all_in_group='groupname')
def view_with_throttle_all_in_group(request):
    return HttpResponse('success')

@throttle(config='anonymous')
def view_with_throttle_config(request):
    return HttpResponse('success')

@throttle(interval=1)
def view_with_throttle_interval(request):
    return HttpResponse('success')

@throttle(scope='scope')
def view_with_throttle_scope_a(request):
    return HttpResponse('success')

@throttle(scope='scope')
def view_with_throttle_scope_b(request):
    return HttpResponse('success')
    