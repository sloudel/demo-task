from django.http import JsonResponse, HttpResponse
from rest_framework.request import Request
from .models import Page
from .serializers import PageListSerializer, PageSerializer
from .tasks import increase_view_counter_task

# Create your views here.

def index(request):
    return JsonResponse({'ok': True})

def page_list(request):
    if request.method == 'GET':
        pages = Page.objects.all()
        serializer = PageListSerializer(pages, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)

def page_detail(request, id):
    try:
        page = Page.objects.get(id=id)
    except Page.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        increase_view_counter_task.delay(page.id)
        serializer = PageSerializer(page, context={'request': request})
        return JsonResponse(serializer.data)

