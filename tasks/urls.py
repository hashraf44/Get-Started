from rest_framework.routers import DefaultRouter
from .views import taskViewSet, userRegistration, userProfile, Dashboard
from django.urls import path

router = DefaultRouter()
router.register(r'task', taskViewSet, basename='task')
urlpatterns = router.urls

urlpatterns = [
    *router.urls,
    path('users/register/', userRegistration.as_view(), name='user-register'),
    path('users/profile/', userProfile.as_view(), name='user-profile'),
    path('dashboard/', Dashboard.as_view(), name='dashboard')
]
