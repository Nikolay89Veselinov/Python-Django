from django.urls import path
from .views import SearchResultsView


from .views import CreatePetViews, EditPetViews, LandingPageViews, PetCommentViews,\
                PetDedailsView, PetDeleteViews, PetLikeViews, PetsListViews, \
                landing_page, pet_list, pet_detail, pet_like, pet_edit, pet_delete, pet_create

app_name = 'petstagram'


urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    # path('', landing_page, name='landing_page'),
    path('', LandingPageViews.as_view(), name='landing_page'),
    # path('pets/', pet_list, name='pet_list'),
    path('pets/', PetsListViews.as_view(), name='pet_list'),
    # path('detail/<int:id>/', pet_detail, name='pet_detail'),
    path('detail/<int:pk>/', PetDedailsView.as_view(), name='pet_detail'),
    path('detail/<slug:slug>/', PetDedailsView.as_view(), name='pet_detail_slug'),
    # path('detail/<int:pk>/<slug:slug>/', PetDedailsView.as_view(), name='pet_detail'),
    # path('like/<int:id>/', pet_like, name='pet_like'),
    path('like/<int:pk>/', PetLikeViews.as_view(), name='pet_like'),
    path('comment/<int:pk>/', PetCommentViews.as_view(), name='pet_comment'),
    # path('edit/<int:id>/', pet_edit, name='pet_edit'),
    path('edit/<int:pk>/', EditPetViews.as_view(), name='pet_edit'),
    # path('delete/<int:id>/', pet_delete, name='pet_delete'),
    path('delete/<int:pk>/', PetDeleteViews.as_view(), name='pet_delete'),
    # path('create/', pet_create, name='pet_create'),
    path('create/', CreatePetViews.as_view(), name='pet_create'),
]