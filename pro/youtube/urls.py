from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt




urlpatterns=[
    path('hello/',csrf_exempt(views.request_video)),
    path('search/',csrf_exempt(views.search)),
    path('sort/',csrf_exempt(views.sort_query))
]