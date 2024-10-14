from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() # amader router

router.register('applylist', views.ApplyViewSet) # router er antena
urlpatterns = [
    path('', include(router.urls)),
    # path('applylist/',views.ApplyViewSet.as_view(),name='apply'),
    
    # path('applylist/',views.apply_view.as_view()),
    
    path("applylistedit/<int:pk>/",views.Edit_for_status_view.as_view(),name="edit"),
    path("deleteapply/<int:pk>/",views.delete_view_apply.as_view(),name="delete"),
    path('apply/', views.ApplyCreateView.as_view(), name='apply-create'),
    
    
]