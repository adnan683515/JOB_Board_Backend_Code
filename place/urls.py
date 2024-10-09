from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('BrowseCetagory', views.BrowseViewSet) # router er antena
router.register('place',views.PlaceViewSet)
router.register('organaigationtype',views.OrganaigationViewSet)
router.register('workplace',views.WorkViewSet)
urlpatterns = [
    path('', include(router.urls)),
]