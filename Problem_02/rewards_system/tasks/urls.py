from django.urls import path
from .views import AppListCreateView, TaskListCreateView


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('', AppListCreateView.as_view(), name='app-list-create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]