from django.urls import path
from .views import news_view, news_delete_view, news_list_view, \
                     news_create_view, new_update_view, news_detail_view

app_name = 'news'
urlpatterns = [
    path('', news_list_view, name='news_list_view'),
    path('create/', news_create_view, name='news_create_view'),
    path('<int:id>/', news_view, name='news_view'),
    path('<int:id>/delete/', news_delete_view, name='news_delete_view'),
    path('<int:id>/update/', new_update_view, name='new_update_view'),
    path('<int:id>/detail/', news_detail_view, name='news_detail_view'),

]
