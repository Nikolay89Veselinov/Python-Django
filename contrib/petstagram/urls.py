from django.urls import path

from .views import landing_page, pet_list, pet_detail, pet_like, pet_edit, pet_delete, pet_create

app_name = 'petstagram'


urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('pets/', pet_list, name='pet_list'),
    path('detail/<int:id>/', pet_detail, name='pet_detail'),
    path('like/<int:id>/', pet_like, name='pet_like'),
    path('edit/<int:id>/', pet_edit, name='pet_edit'),
    path('delete/<int:id>/', pet_delete, name='pet_delete'),
    path('create/', pet_create, name='pet_create'),
]