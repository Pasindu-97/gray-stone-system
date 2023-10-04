from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet

from apps.projects.models import Client, Task, Project
from apps.projects.serializers import ClientSerializer, TaskSerializer, ProjectSerializer


@extend_schema(tags=["client-api"])
class ClientViewSet(ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


@extend_schema(tags=["task-api"])
class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


@extend_schema(tags=["project-api"])
class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
