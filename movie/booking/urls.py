from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('bookticket/',views.bookticket, name="bookticket")
]