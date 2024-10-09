from django.urls import path
from . import views




urlpatterns = [
    path("informationuser/<int:pk>/",views.info_user_for_pk.as_view(),name="user"),
    path('register/',views.RegisterViewSet.as_view(),name='register'),
    path('active/<uidb64>/<token>/',views.activate),
    path('login/',views.LoginViews.as_view(),name='login'),
    path('logout/',views.logoutView.as_view(),name='logout'),
    path('passwordChange/',views.changePasswordView.as_view(),name='password'),
    path("user/<int:pk>/",views.user_view.as_view())
    
]