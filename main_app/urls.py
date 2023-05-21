from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register('notice', NotificationViewSet, basename='notice')

urlpatterns = [
    path('', include(router.urls)),
    path('appeal/create/', AppealListCreateView.as_view(), name='appeal-create'),
]

