from django.http import JsonResponse

def home(request):
    return JsonResponse({
        'message': 'Django Docker App is Live!',
        'status': 'success',
        'project': 'Multi-container Django App with Celery, Redis, PostgreSQL'
    })
from django.shortcuts import render
from django.http import JsonResponse

def home(request):
    # Return HTML page instead of JSON
    return render(request, 'core/home.html')

def health_check(request):
    return JsonResponse({'status': 'healthy', 'services': 'all running'})