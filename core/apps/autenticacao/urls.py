from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

from rest_framework.routers import SimpleRouter

router = SimpleRouter()

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('reset_password/', views.ResetPasswordView.as_view(), name='reset_password'),
    path('reset_password_confirm/<uidb64>/<token>/', views.ResetPasswordConfirmView.as_view(), name='reset_password_confirm'),
]

urlpatterns += router.urls
