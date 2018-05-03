from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.conf import settings

# Create your views here.

# @csrf_exempt
class PingView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse(status=200)