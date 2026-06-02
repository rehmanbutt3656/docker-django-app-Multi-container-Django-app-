from django.http import JsonResponse

def home(request):
    return JsonResponse({
        'message': 'Django Docker App is Live!',
        'status': 'success',
        'project': 'Multi-container Django App with Celery, Redis, PostgreSQL'
    })
