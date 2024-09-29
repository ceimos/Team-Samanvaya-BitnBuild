from django.shortcuts import render,redirect
from django import http
from django.http import JsonResponse
from .models import Cloth
import base64
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
 
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


def home(request):
    return render(request, 'home.html', {})

def user_login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else :
            print("user not authenticated")
        
    return render(request, 'login.html', {})

def user_register_page(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        
    context = {'form' : form}
    return render(request, 'register.html', context)

def new_cloth_page(request):
    return render(request, 'new_cloth.html', {})

def view_wardrobe(request):
    return render(request, 'view-wardrobe.html', {})

def wardrobe_usage(request):
    return render(request, 'wardrobe_usage.html', {})

def sustainability(request):
    return render(request, 'sustainability.html', {})

def outfit_combo(request):
    return render(request, 'outfit_combo.html', {})

def donate(request):
    return render(request, 'donate.html', {})