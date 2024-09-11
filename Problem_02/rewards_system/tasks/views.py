from rest_framework import generics
from .models import App, Task
from .serializers import AppSerializer, TaskSerializer
from rest_framework.permissions import IsAuthenticated

class AppListCreateView(generics.ListCreateAPIView):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = [IsAuthenticated]

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
