from django.contrib import admin
from django.urls import path
from homeDir import views as homeViews
from users import views as userViews
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from homeDir.views import (
    HomeListView,
    MainPostCreateView,
    MainCommentCreateView,
    PostListView,
    PostUpdateView,
    PostDeleteView,
    )

from users.views import MyPostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', userViews.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('profile/', userViews.profile, name='profile'),
    path('password-reset/',userViews.change_password,name='password_reset'),

    path('', HomeListView.as_view(), name='homepage' ),
    path('post/new', MainPostCreateView.as_view(), name='mainpost_create' ),
    path('post/<int:pk>/', MainCommentCreateView.as_view(), name='comment'),
    path('posts/', PostListView.as_view(), name='posts'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post_update'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(), name = 'post_delete'),

    path('profile/<str:username>/', userViews.user_profile, name='user_profile'),
    path('results/', homeViews.search, name='search'),
    path('tags/', homeViews.tag, name='tag'),
    path('myposts/', MyPostListView.as_view(), name='myposts'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
