from django.contrib import admin
from django.urls import path, include
from blog.views import post_list, post_detail, post_add, post_delete, post_edit, signup, comment_remove, posts
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
#jwt & api 관련.
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', post_list),
    path('post/<int:pk>/', post_detail),
    path('post/add/', post_add, name='post_add'),
    path('post/<int:pk>/delete', post_delete, name='post_delete'),
    path('post/<int:pk>/edit/', post_edit, name='post_edit'),
    path('accounts/login/', auth_views.LoginView.as_view(), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('join/', signup, name='join'),
    path('post/<int:pk>/comment/<int:cpk>/remove', comment_remove, name='comment_remove'),
    #jwt & api 관련
    path('api/token/', obtain_jwt_token),
    path('api/token/verify/', verify_jwt_token),
    path('api/token/refresh/', refresh_jwt_token),
    path('api/posts/', posts, name='posts'),

]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
