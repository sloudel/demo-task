from django.urls import path
from .views import index, page_list, page_detail

urlpatterns = [
    path('', index),
    path('pages/', page_list),
    path('pages/<int:id>/', page_detail, name='page-detail'),
]



