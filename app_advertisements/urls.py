from django.urls import path
from .views import index, top_sellers, advertisement, advertisement_post

urlpatterns = [
    path('', index, name='main-page'),
    path('top_sellers/', top_sellers, name='top-sellers'),
    path('advertisement/', advertisement, name='advertisement'),
    path('advertisement_post/', advertisement_post, name='advertisement-post')
]