from rest_framework import (
	generics,
	status,
	pagination,
	mixins,
	viewsets,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
	RoutineSerializer,
	TaskSerializer,
)
from .models import (
	Routine,
	Task,
)



class RoutineViewSetPagination(pagination.PageNumberPagination):
	page_size = 10
	page_size_query_param = "size"
	max_page_size = 25

class RoutineViewSet(viewsets.ModelViewSet):

	queryset = Routine.objects.all()
	serializer_class = RoutineSerializer
	pagination_class = RoutineViewSetPagination


class TaskViewSetPagination(pagination.PageNumberPagination):
	page_size = 10
	page_size_query_param = "size"
	max_page_size = 25

class TaskViewSet(viewsets.ModelViewSet):

	queryset = Task.objects.all()
	serializer_class = TaskSerializer
	pagination_class = TaskViewSetPagination
