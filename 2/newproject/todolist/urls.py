"""from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
"""

from django.urls import path

from . import views

app_name = 'todolist'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:category_id>/', views.detail, name='detail'),
   # path('<int:category_id>/results/', views.results, name='results'),
   path('<int:category_id>/dsc/', views.dsc, name='dsc'),
]