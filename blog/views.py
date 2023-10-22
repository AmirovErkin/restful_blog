from django.shortcuts import render
from rest_framework import generics, permissions, throttling
from django.contrib.auth.models import User
from .models import BlogPost
from .serializers import BlogPostSerializer
# Create your views here.



class BlogPostListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogPostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]


class UserBlogPostListAPIView(generics.ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return BlogPost.objects.filter(user_id=user_id)


class ThrottleConfig(throttling.AnonRateThrottle):
    rate = '3/minute'


class BlogPostThrottledListCreateAPIView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [ThrottleConfig]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogPostThrottledRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [ThrottleConfig]


