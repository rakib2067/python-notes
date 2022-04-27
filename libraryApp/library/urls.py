from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='library-index'),
    path('<int:book_id>', views.show, name='library-show'),
]
