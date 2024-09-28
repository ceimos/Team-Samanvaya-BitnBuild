from django.shortcuts import render
from django import http
from django.http import JsonResponse
from .models import Cloth
import base64
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
# Create your views here.

@login_required
def cloth_list(request):
    user = request.user
    clothes = Cloth.objects.filter(owner=user)
    
    def get_image_data(cloth):
        with open(cloth.image.path, "rb") as image_file:
                return base64.b64encode(image_file.read()).decode('utf-8')

    for cloth in clothes:
        cloth.image = get_image_data(cloth)

    return JsonResponse({'cloth_list': list(clothes.values('id', 'name', 'image', 'type', 'usecount'))})

def save_cloth(request):
    if request.method == 'POST':
        user = request.user
        name = request.POST.get('name')
        image = request.FILES.get('image')
        type = request.POST.get('type')
        usecount = 0 
        
        cloth = Cloth(name=name, image=image, type=type, usecount=usecount, owner=user)
        cloth.save()
        
        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': 'error', 'error': 'Invalid request method'})
    

def get_csrf_token(request):
    return JsonResponse({'csrf_token': get_token(request)})