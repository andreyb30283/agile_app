from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.utils import timezone
from datetime import datetime

# В модуле views создайте файл project_views.py, напишите классовое отображение:
# Реализуйте метод на получение списка всех проектов:
# Получить из query_params значения дат date_from, date_to
# Если никаких значений передано не было - получить список полностью всех проектов
# Если были переданы значения для временного диапазона - сконвертировать полученные значения
# по текущей временной зоне (поможет метод make_aware() и модуль timezone в django)
# Провести фильтрацию по диапазону дат date_from date_to
# Реализуйте метод get на отображение списка всех проектов, добавьте фильтрацию через request_params
# на получение проектов в определённом временном промежутке, например с 2020-01-01 по 2024-01-01
# Реализуйте метод на создание нового проекта
# Зарегиструйте новое отображение в файле urls.py в приложении projects.
# Проверьте работу нашего классового отображения.

from ..serializers.project_serializer import AllProjectsSerializer
from ..models.project import Project

class ProcjectsApi(APIView):

    @staticmethod
    def get_projects(request, date_from=None, date_to=None):
        if not date_from or not date_to:
            projects = Project.objects.all()
            return Response(projects, status=status.HTTP_200_OK)

        date_from = timezone.make_aware(datetime.strptime(date_from, "%y-%m-%d"))

        date_to = timezone.make_aware(datetime.strptime(date_to, "%y-%m-%d"))

        filtrated_projects = Project.objects.filter(created_at__range=[date_from, date_to])

        return Response(filtrated_projects, status=status.HTTP_200_OK)


from django.utils.timezone import make_aware
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from apps.project.models.project import Project
from apps.project.serializers.project_serializer import AllProjectsSerializer, CreateProjectSerializer
from datetime import datetime

class ProjectsApi(APIView):
    serializer_class = AllProjectsSerializer

    def get_queryset(self):
        queryset = Project.objects.all()
        date_from = self.request.query_params.get('date_from', None)
        date_to = self.request.query_params.get('date_to', None)

        if date_from and date_to:
            try:
                date_from = make_aware(datetime.strptime(date_from, '%Y-%m-%d'), timezone.get_current_timezone())
                date_to = make_aware(datetime.strptime(date_to, '%Y-%m-%d'), timezone.get_current_timezone())
                queryset = queryset.filter(created_at__range=(date_from, date_to))
            except ValueError:
                    pass # Handle invalid date format if necessary

        return queryset


    def post(self, request):
        serializer = CreateProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)