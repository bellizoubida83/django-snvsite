from django.contrib import admin
from django.urls import path, include


from . import views 

urlpatterns = [

    path('', views.doc_list),
    path('<int:id>', views.doc_detail)

]