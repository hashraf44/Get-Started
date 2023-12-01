from rest_framework import viewsets, generics
from .models import Task
from .serializers import taskSerializer, userSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Count


class taskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = taskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Task.objects.all()
        priority = self.request.query_params.getstatus('priority', None)
        status = self.request.query_params.get('status', None)

        if priority:
            queryset = queryset.filter(priority=priority)
        if status:
            queryset = queryset.filter(status=status)
        
        return queryset

    def perform_create(self, serializer):
        serializer.save(assigned_to=self.request.user)

class userRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer

class userProfile(generics.RetrieveAPIView):
    serializer_class = userSerializer

    def get_object(self):
        return self.request.user
    
@method_decorator(login_required, name='dispatch')
class Dashboard(View):
    template_name = 'dashboard/dashboard.html'

    def get(self, request, *args, **kwargs):
        tasks = Task.objects.filter(assigned_to = request.user)
        total_tasks = tasks.count()
        completed_tasks = tasks.filter(status = 'completed').count()

        context = {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
        }

        return render(request, self.template_name, context)