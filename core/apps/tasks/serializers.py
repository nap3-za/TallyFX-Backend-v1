from django.conf import settings
from rest_framework import serializers

from .models import (
	Routine,
	Task,
)


class RoutineSerializer(serializers.ModelSerializer):

	class Meta:
		model = Routine
		fields = (
			"id",
			"title",
			"code",
		)
		read_only_fields = (
			"id",
		)

	def update(self, instance, validated_data):
		instance = instance.update(**validated_data)
		return instance


class TaskSerializer(serializers.ModelSerializer):

	class Meta:
		model = Task
		fields = (
			"id",
			"content",
			"state",

			# Relational fields
			"routine",
		)
		read_only_fields = (
			"id",
		)

		depth = 1

	def update(self, instance, validated_data):
		instance = instance.update(**validated_data)
		return instance
