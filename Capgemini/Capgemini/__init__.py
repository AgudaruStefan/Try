from django.core.management import execute_from_command_line
from django.http import HttpResponse
from django.urls import path
from django.conf import settings

settings.configure(DEBUG=True, ROOT_URLCONF='__name__', SECRET_KEY='qwer')

def handle_request(request):
    return HttpResponse("hello, Django")

urlpatterns = [
    path('hello', handle_request),
    ]



if __name__ == '__main__':
    execute_from_command_line()