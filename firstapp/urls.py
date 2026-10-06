from django.urls import path
from . import views

# place for the app level mapping

urlpatterns = [ # this is mapping the urls at the app level (also need to map them at the project level)
    path('function', views.hello_world),
    path('class', views.HelloEthiopia.as_view()), # when passing is classes, need to add an additional method
    path('reservation', views.home),
]