from django.urls import path
from . import views

urlpatterns = [
    
    path('signup/', views.signup_page, name='signup'),
    path('login/', views.login_page, name='login'),
    path('profile/', views.profile_page, name='profile'),
    path('logout/', views.logout_page, name='logout'),
    path('update-profile/', views.update_profile, name='update_profile'),
    path('edit-bio/', views.Edit_bio, name='edit_bio'),
    path('my-posts/', views.My_posts, name='my_posts'),
    path('add-post/', views.add_post, name='add_post'),
    path('update-post/<str:category>/<int:id>/', views.update_post, name='update_post'),
    path('delete-post/<str:category>/<int:id>/', views.delete_post, name='delete_post'),

]
