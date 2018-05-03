from django.http import HttpResponse
from django.template.response import TemplateResponse
# from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

# Create your views here.

# @csrf_exempt
class IndexView(View):
    def get(self, request, *args, **kwargs):
        print('abvcdcaasdasd')
        return TemplateResponse(request, 'index.html')