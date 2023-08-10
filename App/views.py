from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import Home

def index(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index.html')
        else:
            error_message = "Invalid username or password"
            return render(request, './login.html', {'error_message': error_message})
    return render(request, './login.html')

def register_page(request):
    if request.method == 'POST':
        name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        dob = request.POST['dob']
        age = request.POST['age']
        password = request.POST['password']     
        Home.objects.create(name=name, username=username, email=email, dob=dob, age=age, password=password)   
        return render(request, 'register.html', {'success_message': 'Registered Successfully'})  
    return render(request, 'register.html')



# from .forms import HomeForm

# def register(request):
#     if request.method == 'POST':
#         form = HomeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             user_name = form.cleaned_data['name']
#             return render(request, 'after.html', {'user_name': user_name})
#     else:
#         form = HomeForm()
    
#     return render(request, 'after.html', {'form': form})
