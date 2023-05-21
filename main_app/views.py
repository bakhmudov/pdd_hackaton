from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets, permissions
from django.views.generic.detail import DetailView
from .models import Notification, Appeal
from .serializers import NotificationSerializer, AppealSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.AllowAny]


class AppealListCreateView(generics.ListCreateAPIView):
    queryset = Appeal.objects.all()
    serializer_class = AppealSerializer

