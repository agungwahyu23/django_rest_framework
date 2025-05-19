from django.shortcuts import render
from rest_framework import viewsets
from .serializers import LikeSerializer
from .models import Like
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]