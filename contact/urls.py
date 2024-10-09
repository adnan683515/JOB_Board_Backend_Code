from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('contact', views.ContactViewSet) # router er antena
router.register('Ourleaders',views.OurLeaderViewSet)
urlpatterns = [
    path('', include(router.urls)),
]