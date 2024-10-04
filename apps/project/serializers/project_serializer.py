from rest_framework import serializers

from apps.project.models.project import Project


class AllProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'name', 'created_at')


class CreateProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'description', 'created_at')
        read_only_fields = ('created_at',)


    def validate_description(self, value):
        if len(value) < 30:
            raise serializers.ValidationError("Description is too short")
        return value
