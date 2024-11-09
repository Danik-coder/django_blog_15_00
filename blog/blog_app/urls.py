from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('contacts/', views.contacts_page, name='contacts'),
    path('faq/', views.faq_page, name='faq'),
    path('about/', views.about_page, name='about'),
    path('categories/<int:pk>/', views.category_page, name='category'),
    path('post/<str:pk>/', views.post_page, name='post'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logount/', views.logout_page, name='logout'),
    path('post/create_post', views.create_post_page, name='create_post'),
    path('post/delete_post/<int:pk>', views.delete_post, name='delete_post'),
    path('post/update_post/<int:pk>', views.PostUpdateView.as_view(), name='update_post'),
    path('search/', views.search_page, name='search'),
    path('vote/<int:post_id>/<str:action>/', views.add_vote, name='add_vote')
]