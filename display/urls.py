from django.urls import path
from . import views

urlpatterns = [
    path('display-page/<int:page_id>/', views.display_page_view, name='display_page_view'),
]
