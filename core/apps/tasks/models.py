from django.db import models
from django.db.models import Q

from core.apps.misc.field_choices import (
	TaskStates,
)


class RoutineQuerySet(models.QuerySet):
	
	def search(self, query=None):
		if query == None:
			return self.none()
		# - - -
		lookups += Q(Q(field__icontains=query))
		return self.filter(lookups)

class Routine(models.Model):
	
	class RoutineManager(models.Manager):

		def create(self, field):
			model = self.model(
				# - - -
			)
			model.save(using=self._db)
			return model

		def get_queryset(self):
			return RoutineQuerySet(self.model, using=self._db)

		def search(self, query=None):
			return self.get_queryset().search(query=query)


	title 						= models.CharField(verbose_name="title", max_length=125, null=False, blank=False)
	code						= models.CharField(verbose_name="code", max_length=15, unique=True, null=False, blank=False)

	timestamp					= models.DateTimeField(auto_now_add=True)

	objects = RoutineManager()


	def __str__(self):
		return f"{self.id}"


	def update(self, **kwargs):
		Routine.objects.filter(id=self.id).update(**kwargs)
		return Routine.objects.get(id=self.id)


class TaskQuerySet(models.QuerySet):
	
	def search(self, query=None):
		if query == None:
			return self.none()
		lookups += Q(Q(content__icontains=query) | Q(state__icontains=query))
		return self.filter(lookups)

class Task(models.Model):
	
	class TaskManager(models.Manager):

		def create(self, content):
			model = self.model(
				content=content,
			)
			model.save(using=self._db)
			return model

		def get_queryset(self):
			return TaskQuerySet(self.model, using=self._db)

		def search(self, query=None):
			return self.get_queryset().search(query=query)


	content 					= models.CharField(verbose_name="content", max_length=250, null=False, blank=False)
	state 						= models.CharField(verbose_name="state", choices=TaskStates.choices, max_length=3, default=TaskStates.NOT_DONE, null=False, blank=False)
	routine 					= models.ForeignKey(
		"tasks.Routine",
		related_name="tasks",
		related_query_name="task",
		on_delete=models.CASCADE,
		null=False,
		blank=False,
	)

	timestamp					= models.DateTimeField(auto_now_add=True)

	objects = TaskManager()


	def __str__(self):
		return f"{self.id}"
		

	def update(self, **kwargs):
		Task.objects.filter(id=self.id).update(**kwargs)
		return Task.objects.get(id=self.id)