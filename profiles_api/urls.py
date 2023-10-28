from django.urls import path, include
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, base_name='hello-viewset')
router.register("posts-viewset", views.PostViewSet, base_name='posts-viewset')
router.register("cities-viewset", views.CityViewSet, base_name='cities-viewset')
router.register("friend-requests-viewset", views.FriendRequestViewSet, base_name='friend-requests-viewset')
router.register("hash-tags-viewset", views.HashtagsViewSet, base_name='hash-tags-viewset')
router.register("orders-viewset", views.OrdersViewSet, base_name='orders-viewset')


urlpatterns = [
    path('hello-view/', views.HelloAPIView.as_view()),
    path('posts-view/', views.PostAPIView.as_view()),
    path('cities-view/', views.CityAPIView.as_view()),
    path('friend-requests-view/', views.FriendRequestView.as_view()),
    path('hash-tags-view/', views.HashtagsView.as_view()),
    path('orders-view/', views.OrdersView.as_view()),
    path('', include(router.urls))
]
