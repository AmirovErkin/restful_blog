from django.urls import path
from .views import (
    BlogPostListCreateAPIView,
    BlogPostRetrieveUpdateDestroyAPIView,
    UserBlogPostListAPIView,
    BlogPostThrottledListCreateAPIView,
    BlogPostThrottledRetrieveUpdateDestroyAPIView,
)

urlpatterns = [
    path('api/', BlogPostListCreateAPIView.as_view(), name='blogpost-list-create'),
    path('api/<int:pk>/', BlogPostRetrieveUpdateDestroyAPIView.as_view(), name='blogpost-retrieve-update-destroy'),
    path('api/user/<int:user_id>/', UserBlogPostListAPIView.as_view(), name='user-blogpost-list'),
    path('api/throttled/', BlogPostThrottledListCreateAPIView.as_view(), name='throttled-blogpost-list-create'),
    path('api/throttled/<int:pk>/', BlogPostThrottledRetrieveUpdateDestroyAPIView.as_view(),
         name='throttled-blogpost-retrieve-update-destroy'),
]
