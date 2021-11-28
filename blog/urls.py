from django.urls import path
from . import views

# post_listという名前のビューをルートURLに割り当てる
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail')
]