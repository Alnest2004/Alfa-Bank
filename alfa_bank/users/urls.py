from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from users.views import RegisterUserView, ProfileList, ProfileDetail, LoginUser

urlpatterns = [
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    # Регистрация пользователя authorization/auth/users/ С методом POST

    path('register/', RegisterUserView.as_view(), name='register'),
    path('profile_list/', ProfileList.as_view(), name='profile_list'),
    path('profile-detail/<int:pk>/', ProfileDetail.as_view(), name='profile-detail'),
    path('login/', LoginUser.as_view(), name='login'),
]

""" АВТОРИЗАЦИЯ ПО JWT-ТОКЕНУ
# Получаем токен по ссылке http://127.0.0.1:8000/app2/api/v1/token/  
# Затем через postman, по ссылке(например) http://127.0.0.1:8000/app1/support/messages/
передаём в Headers ключ Authorization и значение access токена
"""