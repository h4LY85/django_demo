from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_POST, require_GET

@require_GET
def index(request):
    return HttpResponse("hello")

