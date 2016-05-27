from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
def index(request):
    if request.method == 'GET':
        return HttpResponse("Hello Buffet")
    else:
        print ("get post")
        return JsonResponse({'foo':'bar'})