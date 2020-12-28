from django.urls import path
from . import views
# === Qazi method did not work.
# from django.contrib.auth import views as auth_views
# from django.contrib.auth.views import LoginView
# This (below) is the one that worked. Moved to blog_app\urls.py in part 12.
# from django.contrib.auth.views import LoginView

urlpatterns = [
    # 127.0.0.1:8000
    path('', views.post_list, name='post_list'),

    # 127.0.0.1:8000/post/2
    path('post/<int:pk>/', views.post_detail, name='post_detail'),

    # 127.0.0.1:8000/post/new
    path('post/new/', views.post_new, name='post_new'),

    # 127.0.0.1:8000/post/2/edit
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),

    # 127.0.0.1:8000/drafts
    path('drafts/', views.post_draft_list, name='post_draft_list'),

    # 127.0.0.1:8000/post/2/publish
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),

    # 127.0.0.1:8000/accounts/login
    # === what Qazi suggested but it doesn't work.
    # path('accounts/login/', auth_views.login, name='login'),
    # path('accounts/Login/', auth_views.LoginView, name='Login'),
    # path('accounts/login/', auth_views.login, name='login'),

    # This one (below) worked!  Moved to blog_app\urls.py in part 12.
    # path('accounts/login/', LoginView.as_view(), name='login'),

    # 127.0.0.1:8000/comment/2/remove
    path('post/<int:pk>/comment/', views.add_comment_to_post,
         name='add_comment_to_post'),

    # 127.0.0.1:8000/post/2/comment
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
]
