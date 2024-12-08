from django.urls import path
from .views import hom,books_to_catigores
urlpatterns = [
    path('',hom,name='home'),
    path('category/<int:category_id>',books_to_catigores,name='books_to_catigores')
    #path('category/<int:category_id>/', books_to_catigores, name='books_by_category'),

]